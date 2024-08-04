from locust import HttpUser, task

class User(HttpUser):

    @task
    def load_test(self):
        url = 'http://localhost:8000/uploadfiles/'
        test_file_path = 'data/coco-128/train/000000000009_jpg.rf.856f80d728927e943a5bccfdf49dd677.jpg'
        files = {'files': open(test_file_path, 'rb')}
        r = self.client.post(url, files=files)