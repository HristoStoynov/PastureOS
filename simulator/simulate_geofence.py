"""Simple simulator: load a fence and sample animal points, run point-in-polygon checks and emit events."""
import json
from pathlib import Path
from datetime import datetime

def point_in_polygon(point, polygon):
    x, y = point[0], point[1]
    inside = False
    n = len(polygon)
    for i in range(n):
        xi, yi = polygon[i][0], polygon[i][1]
        xj, yj = polygon[(i+1)%n][0], polygon[(i+1)%n][1]
        intersect = ((yi > y) != (yj > y)) and (x < (xj - xi) * (y - yi) / (yj - yi + 1e-12) + xi)
        if intersect:
            inside = not inside
    return inside


def load_fence(path):
    data = json.loads(Path(path).read_text())
    feat = data["features"][0]
    coords = feat["geometry"]["coordinates"][0]
    # transform from [lon, lat] to [lat, lon]
    poly = [[c[1], c[0]] for c in coords]
    return {"id": feat["properties"]["id"], "polygon": poly}


def run():
    fence = load_fence("simulator/sample_fences.geojson")
    animals = json.loads(Path("simulator/sample_animals.json").read_text())
    events = []
    for a in animals:
        point = [a["lat"], a["lon"]]
        inside = point_in_polygon(point, fence["polygon"])
        evt = {
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "animal_id": a["animal_id"],
            "collar_id": a["collar_id"],
            "inside": inside,
        }
        events.append(evt)
        print(evt)
    Path("simulator/events.json").write_text(json.dumps(events, indent=2))


if __name__ == "__main__":
    run()
