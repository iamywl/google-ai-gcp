# Functional Specification: FlowLens AI

## 1. Overview
FlowLens AI is an engineering-grade service designed to analyze business process logs, identify operational defects (e.g., ping-pong effects, excessive latencies), and generate actionable improvement reports using LLM APIs (Gemini 2.5 Flash).

## 2. API Endpoints

### 2.1. System Health
- **Endpoint**: `GET /v1/health`
- **Response**: `200 OK`
  ```json
  {
    "status": "healthy",
    "version": "1.0.0"
  }
  ```

### 2.2. Log Analysis
- **Endpoint**: `POST /v1/analyze`
- **Input**: `multipart/form-data`
  - `file`: CSV file containing process logs (columns: `department_from`, `department_to`, `timestamp`, `action`).
- **Payload Schema (Output)**:
  ```json
  {
    "statistics": {
      "DeptA -> DeptB": 5,
      "DeptB -> DeptC": 2
    },
    "ai_report": "string (Markdown)",
    "timestamp": "iso8601"
  }
  ```
- **Error Codes**:
  - `400 Bad Request`: Malformed CSV or missing columns.
  - `500 Internal Server Error`: LLM API failure or processing error.

## 3. State Transition Matrix
| Current State | Event | Next State | Action |
|---------------|-------|------------|--------|
| IDLE          | POST /analyze | PROCESSING | Parse CSV, Calculate Stats |
| PROCESSING    | STATS_READY | GENERATING_REPORT | Prompt LLM with Stats |
| GENERATING_REPORT | SUCCESS | COMPLETED | Store Result, Return Response |
| PROCESSING/GENERATING | FAIL | ERROR | Log Error, Return 500 |

## 4. Non-Functional Requirements
- **Efficiency**: CSV processing using `pandas` vectorized operations to minimize O(n) traversal overhead.
- **Reliability**: Exponential backoff for Vertex AI API calls.
- **Security**: Environment variable injection for project IDs and credentials.
