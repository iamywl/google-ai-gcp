import os
import logging
import time
import random
from typing import Any, Dict, List, Optional

import pandas as pd
from google.cloud import aiplatform
from vertexai.generative_models import GenerativeModel

class AnalysisService:
    """비즈니스 로직 및 Vertex AI 연동을 담당하는 서비스 클래스"""

    logger = logging.getLogger(__name__)

    def __init__(self):
        self.project = os.getenv("GCP_PROJECT", "knudc-yoonwoodev")
        self.location = os.getenv("GCP_LOCATION", "us-central1")
        aiplatform.init(project=self.project, location=self.location)
        self.model = GenerativeModel("gemini-1.5-flash")
        logging.info(f"Initialized AnalysisService in {self.project}")

    def generate_ai_report(self, statistics: Dict[str, Any]) -> str:
        """
        통계 데이터를 기반으로 AI 개선 제안 리포트를 생성합니다.
        
        Args:
            statistics: 부서 간 업무 흐름 통계 데이터
            
        Returns:
            AI가 생성한 분석 리포트 문자열
        """
        prompt = f"""
        You are a world-class business process consultant.
        Analyze the following 'ping-pong' effect data between departments and provide strategic improvements:
        Raw Data: {statistics}
        
        Requirements:
        1. Summary of bottlenecks
        2. Actionable checklist for department heads
        3. Analysis of process deviance (skipped or unauthorized steps) based on standard path: Sales -> Purchase -> Legal -> Finance -> Management
        4. Analysis of average idle times per department
        4. Predicted efficiency gain
        Language: Korean
        """
        
        # Exponential Backoff for Production Resilience
        max_retries = 3
        for attempt in range(max_retries):
            try:
                response = self.model.generate_content(prompt)
                return response.text
            except Exception as e:
                if attempt == max_retries - 1:
                    self.logger.error(f"Vertex AI failed after {max_retries} attempts: {e}")
                    raise
                wait_time = 2 ** attempt + random.uniform(0, 1)
                self.logger.warning(f"Vertex AI call failed. Retrying in {wait_time:.2f}s...")
                time.sleep(wait_time)

    def detect_defects(self, df: pd.DataFrame, standard_path: Optional[List[str]] = None) -> Dict[str, Any]:
        """
        과제계획서 명세에 따른 3대 프로세스 결함 진단:
        1. 핑퐁(Ping-pong): 부서 간 반복 왕복
        2. 지연(Idle Time): 특정 구간 장기 정체
        """
        # 1. 핑퐁 탐지 (Ping-pong)
        pingpong_counts = df.groupby(['department_from', 'department_to']).size().to_dict()
        pingpong_stats = {f"{k[0]} -> {k[1]}": int(v) for k, v in pingpong_counts.items() if v > 1}

        # 2. 지연 탐지 (Idle/Delay) - 시간 차이 계산
        df['timestamp'] = pd.to_datetime(df['timestamp'])
        df = df.sort_values(by=['timestamp'])
        # 실제 상용 서비스에서는 case_id별 group이 필요함
        df['duration'] = df['timestamp'].diff().dt.total_seconds().fillna(0) / 3600  # 단위: 시간
        
        avg_delays = df.groupby('department_to')['duration'].mean().to_dict()

        # 3. 일탈 탐지 (Process Deviance)
        standard_path = standard_path if standard_path else ["Sales", "Purchase", "Legal", "Finance", "Management"]
        allowed_transitions = set(zip(standard_path[:-1], standard_path[1:]))
        
        deviations = []
        for _, row in df.iterrows():
            fr, to = str(row['department_from']), str(row['department_to'])
            if (fr, to) not in allowed_transitions:
                if fr in standard_path and to in standard_path:
                    fr_idx = standard_path.index(fr)
                    to_idx = standard_path.index(to)
                    if to_idx > fr_idx + 1:
                        skipped = standard_path[fr_idx + 1:to_idx]
                        deviations.append(f"단계 건너뜀: {fr} -> {to} (누락: {', '.join(skipped)})")
                    elif to_idx <= fr_idx:
                        deviations.append(f"절차 역행(Back-flow): {fr} -> {to}")
                else:
                    deviations.append(f"비인가 경로: {fr} -> {to}")
        
        return {
            "pingpong_defects": pingpong_stats,
            "average_delays_hours": {str(k): round(v, 2) for k, v in avg_delays.items()},
            "process_deviations": deviations,
            "total_cases": len(df)
        }