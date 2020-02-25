from chat import selector
from chat import GoogleMapAPI


class DialogueManager(object):
    def __init__(self, lat, lng, time="now", minprice=0, maxprice=4, keyword=None):
        self.restaurant_selector = selector.RestaurantSelector(lat, lng, time, int(maxprice), keyword)
        self.googledetail = GoogleMapAPI.GoogleDetailAPI()

    def get_inquiry(self):
        return "sample inquiry"

    def gen_recommend_utterance(self):
        try:
            # get restaurants by GoogleMapNearby API
            selected_result = self.restaurant_selector.select()
            # get restaurant detail by GoogleMapDetail API
            # import pdb;pdb.set_trace()
            detail_result = self.googledetail.extract_responses(selected_result["place_id"])
            text = ""
            restaurant_name = selected_result["name"]
            # price_level = str(selected_result["price_level"])
            rating = str(selected_result["rating"])
            text += "近場で良さそうなお店は『" + restaurant_name + "』 で、\n"
            text += "Googleでの評価は" + rating + "だね！\n"
            # text += "値段帯でいうと" + price_level + "ぐらい！"
            # get higest rating review
            reviews = detail_result['result']['reviews']
            if reviews != []:
                text += "以下のようなレビューがあるよ！\n\n『"
                reviews.sort(key=lambda x: x['rating'], reverse=True)
                high_review = reviews[0]
                review_txt = high_review['text']
                text += review_txt + "』\n"
                print("get review: ", review_txt)
            # get google url
            site_url = detail_result['result']['url']
            text += site_url
            print("get url: ", site_url)
        except:
            text = "近くにレストランが見当たらないですね、、"

        return text
