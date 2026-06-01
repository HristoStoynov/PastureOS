# Safety & failsafes

- Audio-first: always play audio warning prior to any pulse
- Cooldown: configurable minimum interval between pulses
- Battery cutoff: never pulse below a safe battery threshold
- Manual override: local physical switch and remote API disable
- Watchdog: pulse driver has hardware watchdog to prevent long pulses
- Logging: all cues/pulses logged with context
