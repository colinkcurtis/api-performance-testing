from locust import HttpLocust, TaskSet, task

class UserBehavior(TaskSet):
    
    @task(1)
    def get_descendants(self):
        self.client.get("/descendants/GO:0005576")
        # TIME TO EXECUTE: GO:0005576 < GO:0005575 < CHEBI:23367

    @task(1)
    def get_children(self):
        self.client.get("/children/GO:0005576")

    @task(1)
    def get_id_list(self):
        self.client.get("/id_list/CL")
        # TIME TO EXECUTE: CL < HP < MONDO < CHEBI

    @task(1)
    def get_label(self):
        self.client.get("/label/MONDO:0004979")


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 0
    max_wait = 1000