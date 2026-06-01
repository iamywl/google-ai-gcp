from fastapi import FastAPI, UploadFile, File, HTTPException, Depends
from .controller import AnalysisController
from .service import AnalysisService
from .repository import AnalysisRepository
from .models import AnalysisResponse

app = FastAPI(title="FlowLens AI - Plan A")

# Dependency Injection Setup
def get_analysis_controller():
    repo = AnalysisRepository()
    service = AnalysisService()
    return AnalysisController(service)

@app.get("/v1/health")
def health_check():
    return {"status": "healthy", "service": "plan_A"}

@app.post("/v1/analyze", response_model=AnalysisResponse)
async def analyze_logs(
    file: UploadFile = File(...),
    controller: AnalysisController = Depends(get_analysis_controller)
):
    try:
        return await controller.handle_analysis(file)
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        # LOGGING: In production, log the full stack trace
        raise HTTPException(status_code=500, detail="Internal Server Error during analysis.")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)
