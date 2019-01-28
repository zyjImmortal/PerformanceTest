from locust import HttpLocust, TaskSet, task
#
#
# class Upload(TaskSet):
#     @task
#     def img(self):
#         self.client.
#
#
# class MusicCard(HttpLocust):
#     pass

import requests
import time
from datetime import datetime

# start = datetime.now()
# response = requests.get('https://t-www.meipian.cn/promo/music_cards/api/cardstatus', params={'object_id':2019012856995650})
# print(response.json()['code'])
# if response.json()['code'] == 0:
#     print(response.json()['data'] )
#     end = datetime.now()
#     print((end - start).seconds)
UPLOAD_URL = 'https://t-www.meipian.cn/promo/music_cards/api/makevideo'
CHECK_COMPLISH = 'https://t-www.meipian.cn/promo/music_cards/api/cardstatus'


def my_task(l):
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    data = {
        'user_id': 30402206,
        'template_id': 1,
        'material': 'http://t-ss2.meipian.me/config/1545803143072.png'
    }
    response = requests.post(url=UPLOAD_URL, data=data, headers=headers).json()
    if response['code'] == 0:
        object_id = response['data']['object_id']
        flag = True
        while flag:
            checked_response = requests.get(CHECK_COMPLISH, params={'object_id': object_id}).json()
            if checked_response['code'] == 0:
                flag = False


class MusicCardTask(TaskSet):
    tasks = [my_task]


class MusicCard(HttpLocust):
    host = 'https://t-www.meipian.cn'
    task_set = MusicCardTask
