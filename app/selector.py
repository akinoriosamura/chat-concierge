import random

from app import GoogleMapAPI


class RestaurantSelector(object):
    def __init__(self):
        self.googlenearbyapi = GoogleMapAPI.GoogleNearbyAPI()

    def get_restaurants_by_api(self, lat, lng, radius):
        """GoogleMapAPIからレストラン一覧を取得

        Args:
            lat ([float]): 検索緯度
            lng ([float]): 検索経度
            radius ([float]): 検索半径

        Returns:
            restaurants ([list]): apiにより取得したレストラン一覧
        """
        restaurants = self.googlenearbyapi.extract_responses(lat, lng, radius)

        return restaurants

    def select(self):
        """responseから必要な要素を取得し集計

        Returns:
            selected_result [dict]: one selected restaurant

        """
        lat = 35.6
        lng = 139.7
        radius = 300
        restaurants = self.get_restaurants_by_api(lat, lng, radius)
        # select logic
        selected_result = random.choice(restaurants)

        return selected_result
