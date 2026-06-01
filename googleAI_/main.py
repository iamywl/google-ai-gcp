import io
import logging
from typing import Any, Dict

import pandas as pd
from fastapi import FastAPI, File, HTTPException, UploadFile, status, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel

from .service import AnalysisService

# 로깅 설정
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="FlowLens AI API",
    description="Enterprise-grade business process analysis API",
    version="1.0.0"
)
service = AnalysisService()

class AnalysisResult(BaseModel):
    statistics: Dict[str, Any]
    ai_report: str

@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    """처리되지 않은 모든 예외를 포착하여 로깅하고 표준화된 에러 응답을 반환합니다."""
    logger.error(f"Global exception caught: {str(exc)}", exc_info=True)
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={
            "status": "error",
            "message": "Internal server error occurred in the service layer.",
            "detail": str(exc)
        }
    )

@app.get("/v1/health")
async def health_check() -> Dict[str, str]:
    """서비스 상태를 점검합니다."""
    return {"status": "healthy", "service": "plan_A", "version": "1.0.0"}

@app.post("/v1/analyze", response_model=AnalysisResult, status_code=status.HTTP_200_OK)
async def analyze_logs(file: UploadFile = File(...)) -> Any:
    """업로드된 CSV 로그 파일을 분석하여 AI 리포트를 생성합니다."""
    if not file.filename.endswith(".csv"):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail="Invalid file format. Only CSV allowed."
        )

    logger.info(f"Processing file: {file.filename}")
    content = await file.read()
    df = pd.read_csv(io.BytesIO(content))
    
    # 비즈니스 로직 실행 (예외 발생 시 global_exception_handler에서 처리)
    stats = service.detect_defects(df)
    report = service.generate_ai_report(stats)
    
    return AnalysisResult(statistics=stats, ai_report=report)