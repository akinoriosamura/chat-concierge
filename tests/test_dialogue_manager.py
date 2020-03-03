from recommender import dialogue_manager

import pytest


@pytest.fixture
def manager():
    return dialogue_manager.DialogueManager()


def test_get_recommend(manager):
    """responseから必要な要素を取得し集計

    Returns:
        recommend_text [str]: recommend text

    """
    recommend_text = manager.get_recommend()
    assert isinstance(recommend_text, str)
    assert recommend_text != ""
