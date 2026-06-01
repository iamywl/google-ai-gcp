from fastapi import UploadFile
import pandas as pd
import io
from .service import AnalysisService
from .models import AnalysisResponse

class AnalysisController:
    def __init__(self, service: AnalysisService):
        # Engineering Principle: Presentation Layer Isolation
        self.service = service

    async def handle_analysis(self, file: UploadFile) -> AnalysisResponse:
        content = await file.read()
        # IDEMPOTENCY: Ensure reading the file doesn't corrupt state
        df = pd.read_csv(io.BytesIO(content))
        
        # Validate CSV columns
        required_cols = {'department_from', 'department_to', 'timestamp', 'action'}
        if not required_cols.issubset(df.columns):
            raise ValueError(f"Missing required columns: {required_cols - set(df.columns)}")
            
        stats = self.service.detect_defects(df)
        report = self.service.generate_report(stats)
        
        return AnalysisResponse(
            statistics=stats,
            ai_report=report
        )
