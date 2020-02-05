import random

from chat import GoogleMapAPI


class RestaurantSelector(object):
    def __init__(self, lat, lng, time, maxprice, keyword):
        self.googlenearbyapi = GoogleMapAPI.GoogleNearbyAPI()
        # filter conditions
        # place (35.62, 139.73) in oosaki
        self.lat = lat
        self.lng = lng
        self.radius = 500
        # time
        self.time = time
        # price
        self.minprice = 0
        self.maxprice = maxprice
        self.keyword = keyword


    def get_restaurants_by_api(self):
        """GoogleMapAPIからレストラン一覧を取得

        Args:

        Returns:
            restaurants ([list]): apiにより取得したレストラン一覧
        """
        restaurants = self.googlenearbyapi.extract_responses(
            self.lat,
            self.lng,
            self.radius,
            self.minprice,
            self.maxprice,
            self.keyword
            )

        return restaurants

    def select(self):
        """responseから必要な要素を取得し集計

        Returns:
            selected_result [dict]: one selected restaurant
             - this is ordered by prominance by googlemapapi

        """
        restaurants = self.get_restaurants_by_api()
        # select restaurants
        # time filter
        if self.time == "now":
            # filter by opennow
            restaurants = [restaurant for restaurant in restaurants if restaurant["open_now"] == True]
            print("num of restaurants: ", len(restaurants))
            # top of order for googlemapapi pronunce order
            selected_result = restaurants[0]
        else:
            selected_result = random.choice(restaurants)

        return selected_result
