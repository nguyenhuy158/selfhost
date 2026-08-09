# AI Scraper 🐒
Intelligent web scraping and data extraction tool powered by Gemini AI.

```mermaid
sequenceDiagram
    participant U as User
    participant S as AI Scraper (FastAPI)
    participant AI as Generative AI
    participant DB as PostgreSQL
    participant W as Target Website

    U->>S: Submit URL & Request
    S->>W: Fetch HTML Content
    W-->>S: Raw HTML
    S->>AI: Send Content + Instruction
    AI-->>S: Clean JSON Data
    S->>DB: Save Result (JSONB)
    S-->>U: Success Toast & UI Update
```

## Architecture
```mermaid
graph LR
    subgraph App_Stack
        FE[AlpineJS FE]
        BE[FastAPI BE]
        Postgres[(PostgreSQL)]
    end
    BE --- Postgres
    FE --- BE
    BE --> Tunnel[Tunnel Service]
```

## Setup
1. Configure your API key in the Settings tab.
2. Run with Docker:
```bash
docker compose up -d --build
```
