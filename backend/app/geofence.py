from typing import List, Dict, Any, Tuple
import math

# Simple in-memory fences store for dev; production should use PostGIS
_FENCES: List[Dict[str, Any]] = [
    {"id": "fence-1", "name": "Test paddock", "polygon": [[45.0, 20.0], [45.0, 20.001], [45.001, 20.001], [45.001, 20.0]]}
]


def list_fences():
    return _FENCES


def point_in_polygon(point: Tuple[float, float], polygon: List[List[float]]) -> bool:
    # Ray casting algorithm: point is (lat, lon); polygon is list of [lat, lon]
    x, y = point[0], point[1]
    inside = False
    n = len(polygon)
    for i in range(n):
        xi, yi = polygon[i][0], polygon[i][1]
        xj, yj = polygon[(i + 1) % n][0], polygon[(i + 1) % n][1]
        intersect = ((yi > y) != (yj > y)) and (x < (xj - xi) * (y - yi) / (yj - yi + 1e-12) + xi)
        if intersect:
            inside = not inside
    return inside
