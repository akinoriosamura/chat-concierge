import json
import datetime

from .base import BaseTestCase


class TestApp(BaseTestCase):

    def post_user(self):
        prms = {
            'id': 1,
            'name': 'test',
        }
        self.app.post('/users',
                      data=json.dumps(prms),
                      content_type='application/json'
                      )

    def test_post_user_201(self):
        prms = {
            'id': 1,
            'name': 'test',
        }
        response = self.app.post('/users',
                                 data=json.dumps(prms),
                                 content_type='application/json'
                                 )
        self.assert_status(response, 200)

    # place
    def test_get_place_404(self):
        self.post_user()
        response = self.app.get('/users/-1/places')
        self.assert_status(response, 404)

    def test_get_place(self):
        self.post_user()
        response = self.app.get('/users/1/places')
        self.assert_status(response, 200)
        assert(
            json.loads(response.get_data()) == {'place': 'here'}
        )

    def test_put_place_204(self):
        self.post_user()
        postPrms = {
            'place': 'tokyo'
        }
        response = self.app.put('/users/1/places',
                                data=json.dumps(postPrms),
                                content_type='application/json'
                                )
        self.assert_status(response, 200)

    # visit_time
    def test_get_visit_time_404(self):
        self.post_user()
        response = self.app.get('/users/-1/visit_times')
        self.assert_status(response, 404)

    def test_get_visit_time(self):
        self.post_user()
        response = self.app.get('/users/1/visit_times')
        self.assert_status(response, 200)
        str_visit_time = json.loads(response.get_data())["visit_time"]
        dt_visit_time = datetime.datetime.strptime(str_visit_time, '%H:%M')
        assert(
            isinstance(dt_visit_time, datetime.datetime)
        )

    def test_put_visit_time_204(self):
        self.post_user()
        postPrms = {
            'visit_time': '12:12:12'
        }
        response = self.app.put('/users/1/visit_times',
                                data=json.dumps(postPrms),
                                content_type='application/json'
                                )
        self.assert_status(response, 200)

    # budget
    def test_get_budget_404(self):
        self.post_user()
        response = self.app.get('/users/-1/budgets')
        self.assert_status(response, 404)

    def test_get_budget(self):
        self.post_user()
        response = self.app.get('/users/1/budgets')
        self.assert_status(response, 200)
        assert(
            json.loads(response.get_data()) == {'budget': '1000'}
        )

    def test_put_budget_204(self):
        self.post_user()
        postPrms = {
            'budget': '2000'
        }
        response = self.app.put('/users/1/budgets',
                                data=json.dumps(postPrms),
                                content_type='application/json'
                                )
        self.assert_status(response, 200)
