from locust import HttpLocust, TaskSet, task

class UserBehavior(TaskSet):
    #1
    @task(1)
    def get_descendants(self):
        self.client.get("/descendants/CHEBI:23367")
    


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 0
    max_wait = 1000