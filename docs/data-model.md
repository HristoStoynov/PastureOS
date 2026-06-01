# Data model

Entities and example fields

- Farm: id, name, location, owner_id
- Pasture: id, farm_id, name, polygon
- VirtualFence: id, pasture_id, name, polygon (GeoJSON), warning_radius_m, breach_radius_m, active
- Animal: id, tag_id, name, species, farm_id
- Collar: id, collar_id, animal_id, firmware_version, last_seen
- TelemetryPoint: id, collar_id, animal_id, timestamp, lat, lon, accuracy, battery_level, connectivity_status, activity_level, temperature_trend, firmware_version
- FenceEvent: id, animal_id, collar_id, event_type, timestamp, location, metadata
- Alert: id, type, severity, animal_id, collar_id, acknowledged, created_at
- Pilot: id, farm_id, start_date, end_date, metrics_summary

Example SQLModel / Pydantic schemas should live in `backend/app/models` and `backend/app/schemas`.
