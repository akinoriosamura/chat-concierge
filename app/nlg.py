from app import selector


class Nlg(object):
    def __init__(self):
        self.restaurant_selector = selector.RestaurantSelector()

    def gen_recommend_utterance(self):
        restaurant_info = self.restaurant_selector.select()
        text = ""
        restaurant_name = restaurant_info["name"]
        price_level = str(restaurant_info["price_level"])
        text += "近場で良さそな店は" + restaurant_name + "だね！"
        text += "値段帯でいうと" + price_level + "ぐらい！"

        return text
