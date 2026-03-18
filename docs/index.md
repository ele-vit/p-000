---
title: p-000 — Items API
nav_order: 1
---

# p-000 — Items API

API REST para gestión de ítems.

## Arquitectura

```mermaid
graph TD
    Client -->|GET /items| API[FastAPI p-000]
    API --> DB[(Items DB)]
```

## Flujo de request

```mermaid
sequenceDiagram
    participant C as Client
    participant A as API
    participant D as DB
    C->>A: GET /items
    A->>D: SELECT * FROM items
    D-->>A: rows
    A-->>C: JSON response
```

## Endpoints

| Método | Path | Descripción |
|--------|------|-------------|
| GET | `/` | Health check |
| GET | `/items` | Lista todos los ítems |
| GET | `/items/{id}` | Obtiene un ítem por ID |
