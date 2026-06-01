import os
from google.cloud import aiplatform
from vertexai.generative_models import GenerativeModel

class AnalysisService:
    def __init__(self):
        self.project = "knudc-yoonwoodev"
        self.location = "us-central1"
        aiplatform.init(project=self.project, location=self.location)
        self.model = GenerativeModel("gemini-1.5-flash")

    def generate_ai_report(self, statistics: dict):
        """
        통계 데이터를 기반으로 AI 개선 제안 리포트를 생성합니다.
        """
        prompt = f"""
        Analyze the following business process defects and provide improvements:
        Data: {statistics}
        
        Please provide:
        1. Summary of bottlenecks
        2. Actionable checklist for department heads
        3. Predicted efficiency gain
        """
        
        response = self.model.generate_content(prompt)
        return response.text

    def detect_pingpong(self, df):
        # 단순화된 핑퐁 탐지 로직 (부서 간 왕복 횟수 계산)
        return df.groupby(['department_from', 'department_to']).size().to_dict()