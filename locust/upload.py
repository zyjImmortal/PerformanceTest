from locust import HttpLocust, TaskSet, task
import random


class UploadImg(TaskSet):

    @task
    def upload(self):
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        data = {
            'user_id': 30402206,
            'template_id': random.randrange(1, 7),
            'material': 'http://t-ss2.meipian.me/config/1545803143072.png'
        }
        with self.client.post('/promo/music_cards/api/makevideo', data=data, headers=headers) as reponse:
            result = reponse.json()
            print(result)


class MusicCard(HttpLocust):
    task_set = UploadImg
    host = 'https://t-www.meipian.cn'
