# Sequence Diagram: PDF Analysis Workflow

```mermaid
sequenceDiagram
    participant C as VS Code Client
    participant G as API Gateway
    participant S as App Service
    participant L as LLM API (Gemini/Claude)
    participant V as Vector DB (pgvector)
    participant R as Redis (Cache)

    C->>G: POST /v1/documents/analyze (PDF)
    G->>S: Forward Request
    S->>S: Extract Text & Chunking
    S->>V: Store Chunks & Generate Embeddings
    S->>R: Cache Processing Status
    S->>L: Request Summary (Context: Extracted Text)
    L-->>S: Return Summary
    S->>V: Update Analysis Result
    S->>R: Set Status: COMPLETED
    S-->>G: Response 202 Accepted (Task ID)
    
    Note over C, S: Client polls for result or waits for Webhook
    C->>G: GET /v1/documents/{id}/summary
    G-->>C: Return JSON Summary
