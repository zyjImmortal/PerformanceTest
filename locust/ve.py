from locust import HttpLocust, TaskSet, task
from datetime import datetime
import json


class VeTaskSet(TaskSet):

    @task
    def make(self):
        data = {
            "tplId": 1,
            "imgUrls": "http://t-ss2.meipian.me/config/1545803143072.png",
            "tplVersion": 1,
            "tplUrl": "https://static-musiccard.ivwen.com/tplmusic/1.zip",
            "recordId": "2019012810055519",
            "createdAt": str(datetime.timestamp),
            "uploadKey": "2019012810055519.mp4"
        }
        headers = {"Content-Type": "application/json"}
        
        with self.client.post('/task/commit', headers=headers, data=json.dumps(data)) as response:
            # result = response.json()
            print(response.raise_for_status())


class VeLocust(HttpLocust):
    host = 'http://172.17.31.157'
    task_set = VeTaskSet
    min_wait = 0
    max_wait = 0
