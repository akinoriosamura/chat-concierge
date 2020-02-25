import os

import googlemaps

import numpy as np


class GoogleNearbyAPI():
    """
    use google place nearby api
    """

    def __init__(self):
        self.key = os.environ["GoogleMapAPIKEY"]  # 上記で作成したAPIキーを入れる
        self.client = googlemaps.Client(self.key)  # インスタンス生成
        # geocode_result = client.geocode('東京都渋谷駅') # 位置情報を検索
        # loc = geocode_result[0]['geometry']['location'] # 軽度・緯度の情報のみ取り出す
        # loc = {'lat': lat, 'lng': lng}
        self.params = {
            'location': (None, None),
            'radius': None,
            'min_price': 0,
            'max_price': 4,
            'keyword': None,
            'type': 'restaurant',
            'language': 'ja',
            'rank_by': 'prominence', # Googleの裏のアルゴリズムによるランキング順
        }
        # 'opening_hours': {'open_now': True}
        self.extracted_attrs = [
            'geo_loc_lat', 'geo_loc_lng', 'id', 'name', 'open_now',
            'photos_heights', 'photos_html_attributions', 'photos_photo_reference',
            'photos_width', 'place_id', 'plus_code_compound_code', 'price_level',
            'rating', 'types', 'user_ratings_total', 'vicinity'
        ]

    def get_response(self):
        """google map nearby apiを呼ぶ

        Returns:
            responses [json]: api result json
            page_token [str]: pake token string or ""

        """
        place_result = self.client.places_nearby(**self.params)
        responses = place_result['results']
        if 'next_page_token' in place_result.keys():
            page_token = place_result["next_page_token"]
        else:
            page_token = ""

        return responses, page_token

    def extract_responses(self, lat, lng, radius, minprice, maxprice, keyword):
        """responseから必要な要素を集計
        Args:
            lat [int]: 緯度
            lng [int]: 経度
            radius [int]: 探索半径
            minprice: [int]: 最小値段範囲/default 1
            maxprice: [int]: 最大値段範囲
            keyword [string]: クエリー
        Returns:
            results [list]: extraceted results
        """
        self.params["location"] = (lat, lng)
        self.params["radius"] = radius
        self.params["min_price"] = minprice
        self.params["max_price"] = maxprice
        self.params["keyword"] = keyword
        results = []
        # api response MAX iter is 3
        api_max_iter = 3
        for _ in range(api_max_iter):
            responses, page_token = self.get_response()
            # responseがなければbreak
            if not responses:
                break
            for response in responses:
                dict_result = {}
                # geometry
                if 'geometry' in response.keys():
                    dict_result["geo_loc_lat"] = response['geometry']['location']['lat']
                    dict_result["geo_loc_lng"] = response['geometry']['location']['lng']
                else:
                    dict_result["geo_loc_lat"] = np.nan
                    dict_result["geo_loc_lng"] = np.nan
                # id
                if 'id' in response.keys():
                    dict_result["id"] = response['id']
                else:
                    dict_result["id"] = ""
                # name
                if 'name' in response.keys():
                    dict_result["name"] = response['name']
                else:
                    dict_result["name"] = ""
                # open_now
                if 'opening_hours' in response.keys():
                    dict_result["open_now"] = response['opening_hours']['open_now']
                else:
                    dict_result["open_now"] = None
                # photos
                if 'photos' in response.keys():
                    p_value = response['photos'][0]
                    dict_result["photos_heights"] = p_value['height']
                    dict_result["photos_html_attributions"] = p_value['html_attributions'][0]
                    dict_result["photos_photo_reference"] = p_value['photo_reference']
                    dict_result["photos_width"] = p_value['width']
                else:
                    dict_result["photos_heights"] = np.nan
                    dict_result["photos_html_attributions"] = ""
                    dict_result["photos_photo_reference"] = ""
                    dict_result["photos_width"] = np.nan
                # place_id
                if 'place_id' in response.keys():
                    dict_result["place_id"] = response['place_id']
                else:
                    dict_result["place_id"] = ""
                # plus_code
                if 'plus_code' in response.keys():
                    dict_result["plus_code_compound_code"] = response['plus_code']['compound_code']
                else:
                    dict_result["plus_code_compound_code"] = ""
                # price level
                if 'price_level' in response.keys():
                    dict_result["price_level"] = response['price_level']
                else:
                    dict_result["price_level"] = np.nan
                # rating
                if 'rating' in response.keys():
                    dict_result["rating"] = response['rating']
                else:
                    dict_result["rating"] = np.nan
                # types
                if 'types' in response.keys():
                    dict_result["types"] = response['types']
                else:
                    dict_result["types"] = ""
                # user_ratings_total
                if 'user_ratings_total' in response.keys():
                    dict_result["user_ratings_total"] = response['user_ratings_total']
                else:
                    dict_result["user_ratings_total"] = np.nan
                # vicinity
                if 'vicinity' in response.keys():
                    dict_result["vicinity"] = response['vicinity']
                else:
                    dict_result["vicinity"] = ""

                results.append(dict_result)

            # 次のページがない場合break
            if page_token == "":
                break

        return results


class GoogleDetailAPI():
    """
    use google place nearby api
    """
    def __init__(self):
        self.key = os.environ["GoogleMapAPIKEY"]  # 上記で作成したAPIキーを入れる
        self.client = googlemaps.Client(self.key)  # インスタンス生成
        self.params = {
            'place_id': None,
            'language': 'ja'
        }

    def extract_responses(self, place_id):
        """responseから必要な要素を集計
        Args:
            place_id [string]: 場所のid
        Returns:
            detail_result [dict]: extraceted result etail
        """
        self.params["place_id"] = place_id
        detail_result = self.client.place(**self.params)

        return detail_result
