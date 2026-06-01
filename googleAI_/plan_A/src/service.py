import pandas as pd
from google import genai
from .models import AnalysisResponse
import os
from typing import Dict

class AnalysisService:
    def __init__(self):
        # Engineering Principle: Business Logic & Core Infrastructure Binding
        # Using environment variables for project configuration
        self.project_id = os.getenv("GCP_PROJECT", "knudc-yoonwoodev")
        self.location = os.getenv("GCP_LOCATION", "us-central1")
        
        self.client = genai.Client(
            vertexai=True,
            project=self.project_id,
            location=self.location
        )

    def detect_defects(self, df: pd.DataFrame) -> Dict[str, int]:
        """
        Detects 'ping-pong' defects where work bounces back and forth between departments.
        Utilizes pandas vectorized operations for O(1) or O(n) performance.
        """
        # Simple ping-pong: count occurrences of (dept_a -> dept_b)
        pingpong = df.groupby(['department_from', 'department_to']).size().to_dict()
        # Convert tuple keys to string for JSON compatibility
        return {f"{k[0]} -> {k[1]}": v for k, v in pingpong.items()}

    def generate_report(self, stats: Dict[str, int]) -> str:
        """
        Generates an AI-driven improvement report using Gemini.
        """
        prompt = f"""
        Analyze the following business process defects and provide improvements:
        Defect Data (Ping-pong counts between departments):
        {stats}
        
        Please provide the report in Markdown format with the following sections:
        1. Executive Summary of Bottlenecks
        2. Root Cause Analysis (Technical Perspective)
        3. Actionable Mitigation Checklist
        4. Predicted Efficiency Gains (Deterministic Estimate)
        
        Constraint: No metaphors. Use engineering principles.
        """
        
        try:
            response = self.client.models.generate_content(
                model='gemini-2.0-flash', # Updated to a known stable model if 2.5 is not yet GA
                contents=prompt
            )
            return response.text
        except Exception as e:
            # Fallback or error handling
            return f"LLM Generation Failed: {str(e)}"
