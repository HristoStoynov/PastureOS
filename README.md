PastureOS
===========

PastureOS is a smart livestock collar and AI platform for European farms. It combines virtual fencing, guided movement, live tracking, and pilot instrumentation to evaluate the operational value of wearable collars for cattle.

MVP objective
-------------
Deliver a safe, auditable collar + cloud platform that can reliably contain cattle with virtual geofences, provide audio-first cues and controlled low-intensity pulses (with strict safety limits), and prove operational value via pilot metrics.

System components
-----------------
- Collar firmware (embedded): GPS, IMU, temperature, speaker, low-intensity pulse circuit, modem
- Cloud backend: FastAPI + Postgres/PostGIS (SQLite for dev)
- Dashboard: Next.js + TypeScript + Mapbox/Leaflet
- AI/Analytics: Rule-based baselines → ML (PyTorch/scikit-learn)
- Simulator: geofence and herd behaviour simulator
- Pilot instrumentation & scorecard
- DevOps infra: Docker Compose, CI/CD

Quickstart (local development)
------------------------------
1. Backend: `cd backend && docker-compose up` (starts API + DB) or run `uvicorn app.main:app --reload` inside `backend`
2. Frontend: `cd frontend && npm install && npm run dev`
3. Simulator: `python3 simulator/simulate_geofence.py` to run a simulated event generation

High-level architecture
-----------------------

```mermaid
graph LR
  Collar[Collar Device] -->|MQTT/HTTP Telemetry| Ingest[Telemetry Ingest (FastAPI)]
  Ingest --> DB[(Postgres + PostGIS)]
  Ingest --> GeofenceEngine[Geofence Engine]
  GeofenceEngine --> EventEngine[Event Engine]
  EventEngine --> Alerts[Alerts & Notifications]
  DB --> AI[AI / Analytics]
  UI[Dashboard (Next.js)] --> DB
  UI --> Alerts
```

Current assumptions
-------------------
- Pilot in Eastern Europe with cellular coverage (LTE-M/NB-IoT or LoRaWAN where available).
- Prioritise safety, battery life and ruggedness for v0.
- No medical or diagnostic claims from AI in v0.

Out of scope for v0
-------------------
- Medical diagnosis, automated treatments
- Sheep/goat variants
- Regulatory certification and mass manufacturing details

Repository layout
-----------------
See the repository tree in `docs/` and the top-level folders for starter code and documentation.
