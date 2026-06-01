# API specification (selected endpoints)

Auth
- POST /auth/login — exchange credentials for JWT

Farms
- GET /farms
- POST /farms

Animals
- GET /animals
- POST /animals
- GET /animals/{id}
- GET /animals/{id}/telemetry
- GET /animals/{id}/events

Collars
- GET /collars
- POST /collars
- PATCH /collars/{id}

Telemetry
- POST /telemetry/ingest — device ingestion endpoint
- GET /telemetry/latest

Virtual fences
- GET /fences
- POST /fences
- PATCH /fences/{id}
- DELETE /fences/{id}

Alerts
- GET /alerts
- PATCH /alerts/{id}/acknowledge

Pilots
- POST /pilots
- GET /pilots/{id}/scorecard
- GET /pilots/{id}/export

AI
- GET /animals/{id}/anomalies
- POST /ai/anomaly-review
