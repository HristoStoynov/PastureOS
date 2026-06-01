# Power budget

Provide rough power budget planning for idle, tracking and active cue/pulse events. Prototype should prioritise power savings:

- Deep sleep between GPS fixes
- Adaptive GPS interval based on movement
- Batch telemetry uploads when on cellular

Estimate:
- Idle (deep sleep): <1 mA
- GPS-on (fix): 30–50 mA for 1–3 seconds per fix
- LTE transmit (short): 100–300 mA during transmission
- Audio cue: short bursts, small energy
- Pulse: limited duration and duty cycle (safety first)
