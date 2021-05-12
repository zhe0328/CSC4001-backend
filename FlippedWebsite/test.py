import unittest
import requests


class TestMethods(unittest.TestCase):
    def setUp(self):
        self.base_url = 'http://127.0.0.1:8000/'

    def test_2_upload_video_info(self):
        # response = self.client.post()
        form_data = {'username': 'temp', 'time': '135',
                     'link':'media/temp/demo.mp4',
                     'title': 'Google Developer Platform', 'price': '10', "type": "Video Editing", "deadline": "2021-5-20", "summary": "This task is film editing of a 10 minutes video. The topic is relevant to Google developer."}
        # print(form_data)
        r = requests.post(self.base_url+'upload_video_info/', json=form_data)
        result = r.json()
        # print(r.json())
        self.assertEqual(result['status'], 100)

    def test_1_add_user(self):
        # response = self.client.post()
        form_data = {'username': 'unittest3', 'email': 'zxw668@qq.com',
                     'password': 'qawsedrftg', 'gender': 'female'}
        r = requests.post(self.base_url+'create_user/', json=form_data)
        result = r.json()
        # print(r.json())
        self.assertEqual(result['status'], 100)

    def test_3_add_transaction_abnormal(self):
        form_data = {'username':'test', 'title': 'Google'}
        r = requests.post(self.base_url+'add_transaction/', json=form_data)
        result = r.json()
        # print(r.json())
        self.assertEqual(result['status'], 200)

    def test_3_add_transaction(self):
        form_data = {'username':'test', 'title': 'Google Developer Platform'}
        r = requests.post(self.base_url+'add_transaction/', json=form_data)
        result = r.json()
        # print(r.json())
        self.assertEqual(result['status'], 100)

    def test_4_show_trade_platform(self):
        r = requests.get(self.base_url+'show_trade_platform')
        result = r.json()
        print(result)

    def test_5_show_trade_video(self):
        form_data = {'task_id':1}
        r = requests.post(self.base_url+'show_trade_video/', json=form_data)
        result = r.json()
        print(result)

    def test_6_show_todo_list(self):
        form_data = {'username': 'test'}
        r = requests.post(self.base_url+'show_todo_list/', json=form_data)
        result = r.json()
        print(result)

    def test_7_update_todo_list(self):
        form_data = {'task_id': 1}
        r = requests.post(self.base_url+'update_todo_list/', json=form_data)
        result = r.json()
        self.assertEqual(result['status'], 100)


if __name__ == '__main__':
    unittest.main()
