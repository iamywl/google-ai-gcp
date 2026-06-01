# Functional Specification: PDF AI Intelligence Service

## 1. Overview
This service provides asynchronous PDF text extraction, summarization, and RAG (Retrieval-Augmented Generation) capabilities via LLM APIs (Gemini 1.5 Pro/Claude 3.5 Sonnet). It is designed to interface with the `vscode-pdf` extension.

## 2. API Endpoints

### 2.1. Document Processing
- **Endpoint**: `POST /v1/documents/analyze`
- **Input**: `multipart/form-data` (file: PDF)
- **Payload Schema**:
  ```json
  {
    "document_id": "uuid",
    "status": "processing | completed | failed",
    "summary": "string",
    "metadata": { "pages": "int", "author": "string" }
  }
  ```
- **Error Codes**: `413 (Payload Too Large)`, `415 (Unsupported Media Type)`, `503 (LLM Provider Timeout)`.

### 2.2. Contextual Chat (RAG)
- **Endpoint**: `POST /v1/chat/query`
- **Input**: `application/json`
  ```json
  {
    "document_id": "uuid",
    "prompt": "string",
    "stream": "boolean"
  }
  ```
- **Output**: SSE (Server-Sent Events) or JSON response containing the LLM generated answer based on document chunks.

## 3. State Transition Matrix
| Current State | Event | Next State | Action |
|---------------|-------|------------|--------|
| IDLE          | UPLOAD| PROCESSING | Extract Text, Generate Embeddings |
| PROCESSING    | SUCCESS| COMPLETED  | Store in Vector DB, Notify Client |
| PROCESSING    | FAIL   | ERROR      | Log Error, Exponential Backoff Retry |
| COMPLETED     | QUERY  | STREAMING  | Vector Search, Prompt LLM |

## 4. Non-Functional Requirements
- **Latency**: LLM response start-of-stream < 2s.
- **Scalability**: Stateless API nodes for horizontal scaling.
- **Security**: JWT-based authentication, AES-256 encryption for stored documents.