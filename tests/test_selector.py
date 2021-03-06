from recommender import selector

import pytest


@pytest.fixture
def restaurant_selector():
    return selector.RestaurantSelector()


def test_select(restaurant_selector):
    """responseから必要な要素を取得し集計

    Returns:
        selected_result [dict]: one selected restaurant

    """
    selected_result = restaurant_selector.select()
    assert isinstance(selected_result, dict)
    assert selected_result != {}
