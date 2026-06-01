# MVP scope

Minimal features required to evaluate pilot success:
- GPS/GNSS tracking and live location
- Virtual geofence creation and storage
- Boundary detection with warning & breach zones
- Audio cue (device-side) event triggered when approaching fence
- Controlled low-intensity pulse (device-side) only after audio cue, with cooldown
- Live dashboard with map and event timeline
- Alerts: escape/breach, low battery, connectivity loss
- Farmer override/pause mode
- Pilot scorecard export (CSV/JSON)

Safety constraints:
- Pulse only after audio cue
- Pulse frequency and duration configurable and limited
- Training mode and manual override
