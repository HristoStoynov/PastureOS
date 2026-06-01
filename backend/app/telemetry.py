from pydantic import BaseModel
from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime


class TelemetryIn(BaseModel):
    animal_id: str
    collar_id: str
    timestamp: datetime
    latitude: float
    longitude: float
    gps_accuracy: Optional[float] = None
    battery_level: Optional[float] = None
    connectivity_status: Optional[str] = None
    activity_level: Optional[float] = None
    temperature_trend: Optional[float] = None
    firmware_version: Optional[str] = None
    event_type: Optional[str] = None


class TelemetryPoint(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    animal_id: str
    collar_id: str
    timestamp: datetime
    latitude: float
    longitude: float
    gps_accuracy: Optional[float] = None
    battery_level: Optional[float] = None
    connectivity_status: Optional[str] = None
    activity_level: Optional[float] = None
    temperature_trend: Optional[float] = None
    firmware_version: Optional[str] = None
    event_type: Optional[str] = None

    @classmethod
    def from_telemetry(cls, t: TelemetryIn):
        return cls(
            animal_id=t.animal_id,
            collar_id=t.collar_id,
            timestamp=t.timestamp,
            latitude=t.latitude,
            longitude=t.longitude,
            gps_accuracy=t.gps_accuracy,
            battery_level=t.battery_level,
            connectivity_status=t.connectivity_status,
            activity_level=t.activity_level,
            temperature_trend=t.temperature_trend,
            firmware_version=t.firmware_version,
            event_type=t.event_type,
        )
