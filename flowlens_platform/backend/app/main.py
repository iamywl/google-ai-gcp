from fastapi import FastAPI

app = FastAPI(title="FlowLens AI Backend", description="API for Process Mining & AI Reports")

@app.get("/")
def read_root():
    return {"status": "ok", "message": "FlowLens AI API Server is running"}

# Mock endpoints covering 10 modules
@app.get("/api/v1/health")
def health_check():
    return {"status": "healthy", "modules": 10, "features": 117}

@app.post("/api/v1/auth/login")
def login(): pass

@app.get("/api/v1/mining/pingpong")
def get_pingpong_data():
    return {"data": [{"dept": "구매팀", "bounce": 14, "risk": "High"}]}
    
@app.get("/api/v1/ai/report")
def generate_report():
    return {"report": "구매팀과 재무팀 간의 반려가 14회 발생하여 전체 지연의 30%를 차지합니다."}
