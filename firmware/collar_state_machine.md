# Collar state machine

States:
- IDLE
- TRACKING
- APPROACHING_BOUNDARY
- AUDIO_WARNING
- PULSE_READY
- PULSE_TRIGGERED
- BREACH_ALERT
- TRAINING_MODE
- MANUAL_OVERRIDE
- LOW_BATTERY
- CONNECTIVITY_LOSS
- FAILSAFE_DISABLED

Important rules:
- Audio warning must always precede any pulse
- Configurable safety cooldown between pulses
- No pulse if battery below safe threshold or manual override enabled
