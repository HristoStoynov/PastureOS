# Geofencing logic

Terminology
- Geofence: polygon (GeoJSON)
- Warning zone: inward buffer from the fence (configurable, e.g., 10–25 m)
- Breach zone: crossing the fence polygon boundary

Core checks
- Point-in-polygon test to determine inside/outside
- Distance-to-boundary calculation to detect approach
- Warning when within `warning_radius` and still inside
- Breach when outside polygon or crossing into breach zone

Behavioural rules
- Audio warning triggered on approaching boundary
- Pulse allowed only after audio warning and only if animal continues toward breach within configured cooldown and intensity limits
- Training mode: only audio, no pulses
- Manual override: disable cues/pulses per-collar or herd
- No-pulse conditions: low battery, distress signals, animal in vet/exclusion list

Cooldown
- Configurable per-collar cooldown (e.g., 5–30 minutes) between pulses
