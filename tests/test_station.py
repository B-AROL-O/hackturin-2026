"""Dashboard station endpoint: reads the JSON written by station_rx.py --latest."""

import json
import os
import time

from fastapi.testclient import TestClient

from poopvolt.server import Settings, create_app


def make_client(tmp_path):
    settings = Settings(
        model=tmp_path / "absent.onnx",
        config=tmp_path / "absent.json",
        storage=tmp_path / "data",
        station=tmp_path / "latest.json",
    )
    return settings, TestClient(create_app(settings))


def test_station_missing_file_is_unavailable(tmp_path):
    _, client = make_client(tmp_path)
    with client:
        body = client.get("/api/station").json()
    assert body == {"available": False, "age_s": None, "reading": None}


def test_station_fresh_and_stale(tmp_path):
    settings, client = make_client(tmp_path)
    reading = {"temp_c": 24.3, "pv_ma": 0.0, "perf_pct": None, "calibrated": False}
    settings.station.write_text(json.dumps(reading))
    with client:
        fresh = client.get("/api/station").json()
        old = time.time() - 60
        os.utime(settings.station, (old, old))
        stale = client.get("/api/station").json()
    assert fresh["available"] and fresh["reading"] == reading
    assert not stale["available"] and stale["reading"] == reading


def test_station_corrupt_file_is_unavailable(tmp_path):
    settings, client = make_client(tmp_path)
    settings.station.write_text("{not json")
    with client:
        assert client.get("/api/station").json()["available"] is False
