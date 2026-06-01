import pytest
from fastapi.testclient import TestClient
from src.main import app
import io
import pandas as pd

client = TestClient(app)

def test_health_check():
    response = client.get("/v1/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"

def test_analyze_invalid_csv():
    # Test with missing columns
    csv_content = "col1,col2\nval1,val2"
    files = {'file': ('test.csv', io.BytesIO(csv_content.encode()), 'text/csv')}
    response = client.post("/v1/analyze", files=files)
    assert response.status_code == 400
    assert "Missing required columns" in response.json()["detail"]

def test_analyze_valid_csv_mocked_ai(mocker):
    # Mocking the AI service generate_report method
    mock_report = "Mocked AI Report: Efficiency increase predicted."
    mocker.patch("src.service.AnalysisService.generate_report", return_value=mock_report)
    
    csv_content = "department_from,department_to,timestamp,action\nDeptA,DeptB,2023-01-01 10:00:00,transfer"
    files = {'file': ('test.csv', io.BytesIO(csv_content.encode()), 'text/csv')}
    
    response = client.post("/v1/analyze", files=files)
    assert response.status_code == 200
    data = response.json()
    assert "DeptA -> DeptB" in data["statistics"]
    assert data["ai_report"] == mock_report
