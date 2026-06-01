from fastapi import FastAPI, UploadFile, File
import pandas as pd
import io
from .service import AnalysisService

app = FastAPI(title="FlowLens AI API")
service = AnalysisService()

@app.get("/v1/health")
def health_check():
    return {"status": "healthy", "service": "plan_A"}

@app.post("/v1/analyze")
async def analyze_logs(file: UploadFile = File(...)):
    content = await file.read()
    df = pd.read_csv(io.BytesIO(content))
    
    # 로직 실행
    stats = service.detect_pingpong(df)
    report = service.generate_ai_report(stats)
    
    return {
        "statistics": stats,
        "ai_report": report
    }