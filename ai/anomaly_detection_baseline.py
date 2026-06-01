"""
Baseline anomaly detection: simple rolling-window z-score on activity_level.
"""
import collections
import statistics
from datetime import datetime, timedelta


class BaselineDetector:
    def __init__(self, window=24):
        # window in hours
        self.window = window
        self.points = collections.defaultdict(list)  # animal_id -> list of (ts, value)

    def add_point(self, animal_id, timestamp, activity_level):
        self.points[animal_id].append((timestamp, activity_level))
        cutoff = timestamp - timedelta(hours=self.window)
        self.points[animal_id] = [(t, v) for (t, v) in self.points[animal_id] if t >= cutoff]

    def check_anomaly(self, animal_id):
        data = [v for (t, v) in self.points.get(animal_id, []) if v is not None]
        if len(data) < 6:
            return None
        mean = statistics.mean(data)
        stdev = statistics.pstdev(data)
        latest = data[-1]
        if stdev == 0:
            return None
        z = (latest - mean) / stdev
        if abs(z) > 3:
            return {"animal_id": animal_id, "z": z, "severity": "high"}
        if abs(z) > 2:
            return {"animal_id": animal_id, "z": z, "severity": "medium"}
        return None


if __name__ == "__main__":
    d = BaselineDetector(window=24)
    now = datetime.utcnow()
    for h in range(30):
        t = now - timedelta(hours=30 - h)
        d.add_point("cow-1", t, activity_level=1.0 + (0.1 if h % 10 == 0 else 0))
    print(d.check_anomaly("cow-1"))
