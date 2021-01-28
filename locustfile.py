from os import environ

from locust import HttpUser, task, between


class PelandoMainPageUser(HttpUser):
    weight = 3
    wait_time = between(1, 3)
    host = environ['HOST']

    @task()
    def test(self):
        self.client.get('/', name='main')


class PelandoRecentPageUser(HttpUser):
    weight = 1
    wait_time = between(1, 3)
    host = environ['HOST']

    @task()
    def test(self):
        self.client.get('/recentes', name='recent')


class PelandoHotPageUser(HttpUser):
    weight = 2
    wait_time = between(1, 3)
    host = environ['HOST']

    @task()
    def test(self):
        self.client.get('/quente', name='hot')
