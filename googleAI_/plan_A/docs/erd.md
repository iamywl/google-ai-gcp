# Entity Relationship Diagram - FlowLens AI

```mermaid
erDiagram
    PROCESS_LOG {
        uuid id PK
        string department_from
        string department_to
        timestamp event_time
        string action
    }
    ANALYSIS_REPORT {
        uuid id PK
        uuid log_id FK
        text summary
        jsonb defects
        timestamp created_at
    }
```
