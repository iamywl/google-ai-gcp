from pydantic import BaseModel, Field
from typing import List, Dict, Optional
from datetime import datetime

class AnalysisRequest(BaseModel):
    # For CSV upload, we might not use this Pydantic model directly for the body
    # but it's good for internal data validation.
    pass

class PingPongStat(BaseModel):
    department_pair: str
    count: int

class AnalysisResponse(BaseModel):
    statistics: Dict[str, int]
    ai_report: str
    timestamp: datetime = Field(default_factory=datetime.now)

class ProcessLogEntry(BaseModel):
    department_from: str
    department_to: str
    timestamp: datetime
    action: str
