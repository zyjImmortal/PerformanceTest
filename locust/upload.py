from locust import HttpLocust, TaskSet, task
from datetime import datetime


class UploadImg(TaskSet):
    test_start_time = None

    def on_start(self):
        test_start_time = datetime.now()
        print('test_start_time:{}'.format(test_start_time))


    @task
    def upload(self):
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        data = {
            'user_id': 30402206,
            'template_id': 1,
            'material': 'http://t-ss2.meipian.me/config/1545803143072.png'
        }
        start = datetime.now()
        with self.client.post('/promo/music_cards/api/makevideo', data=data, headers=headers) as reponse:
            result = reponse.json()
            if result['code'] == 0:
                object_id = result['data']['object_id']
                print(object_id)
                flag = True
                while flag:
                    with self.client.get('/promo/music_cards/api/cardstatus', params={'object_id': object_id}) as rs:
                        check = rs.json()
                        if check['code'] == 0:
                            end = datetime.now()
                            spend = (end - start).seconds
                            print('时间为:{}'.format(spend))
                            print(check['data'])
                            flag = False

    def on_stop(self):
        test_end_time = datetime.now()
        print('test_end_time:{}'.format(test_end_time))


class MusicCard(HttpLocust):
    task_set = UploadImg
    host = 'https://t-www.meipian.cn'
