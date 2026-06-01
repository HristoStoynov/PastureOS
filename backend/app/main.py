from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import SQLModel, Session, create_engine
from app import database
from app import telemetry as telemetry_mod
from app.geofence import geofence

app = FastAPI(title="PastureOS API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def on_startup():
    database.init_db()


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/telemetry/ingest")
def telemetry_ingest(payload: telemetry_mod.TelemetryIn):
    # persist and run basic geofence check
    db = database.get_session()
    tp = telemetry_mod.TelemetryPoint.from_telemetry(payload)
    db.add(tp)
    db.commit()
    # simple geofence check (placeholder)
    fences = geofence.list_fences()
    events = []
    for f in fences:
        if geofence.point_in_polygon((payload.latitude, payload.longitude), f["polygon"]):
            events.append({"event": "INSIDE_FENCE", "fence": f["id"]})
        else:
            events.append({"event": "OUTSIDE_FENCE", "fence": f["id"]})
    return {"ingested": True, "events": events}


@app.get("/fences")
def get_fences():
    return geofence.list_fences()
