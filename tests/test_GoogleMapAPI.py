from chat import GoogleMapAPI

import pytest


@pytest.fixture
def google_nearby_api():
    return GoogleMapAPI.GoogleNearbyAPI()


def test_get_response(google_nearby_api):
    # lat: 30, lng: 140, radius: 50
    google_nearby_api.params["location"] = (30.0, 140.0)
    google_nearby_api.params["radius"] = 50
    responses, page_token = google_nearby_api.get_response()
    assert responses == []
    assert page_token == ""

    # lat: 35.6, lng: 139.7, radius: 200
    google_nearby_api.params["location"] = (35.6, 139.7)
    google_nearby_api.params["radius"] = 200
    responses, page_token = google_nearby_api.get_response()
    assert responses != []
    assert page_token == ""

    # lat: 35.6, lng: 139.7, radius: 300
    google_nearby_api.params["location"] = (35.6, 139.7)
    google_nearby_api.params["radius"] = 300
    responses, page_token = google_nearby_api.get_response()
    assert responses != []
    assert page_token != ""


def test_extract_responses(google_nearby_api):
    """responseから必要な要素を取得し集計

    Args:
        lat [int]: 緯度
        lng [int]: 経度
        radius [int]: 探索半径
    Returns:
        results [list]: extraceted results

    """
    lat = 35.6
    lng = 139.7
    radius = 300
    results = google_nearby_api.extract_responses(lat, lng, radius)
    assert results != []
    assert set(google_nearby_api.extracted_attrs) == set(results[0].keys())
