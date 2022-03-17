from shapely.geometry import Polygon, MultiPolygon, mapping

def test_create_proposal(client):
    poly = MultiPolygon([Polygon([(-105,39),(-105,40),(-104,40),(-104,39),(-105,39)])])
    payload = {
        "title":"Test",
        "pest_type":"weed",
        "chemical":"glyphosate",
        "geometry": mapping(poly)
    }
    r = client.post("/api/v1/proposals/", json=payload)
    assert r.status_code in (200,201)
    assert "id" in r.json()
