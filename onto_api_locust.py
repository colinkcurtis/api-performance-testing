from locust import HttpLocust, TaskSet, task

class UserBehavior(TaskSet):

    @task(1)
    def get_ancestors(self):
        self.client.get("/ancestors/MONDO%3A0004634")

    @task(1) #the values inside the parantheses give a relative weight to the frequency of execution of each task by the locust-swarm!
    def get_all_properties(self):
        self.client.get("/all_properties/CHEBI:89671")

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 0
    max_wait = 1000



    # The functions defined below are basic setup and tear-down in the event that the API which you need to test is protected by a user/pass login/logout structure!
    # def on_start(self):
    #     """ on_start is called when a Locust start before any task is scheduled """
    #     self.login()

    # def on_stop(self):
    #     """ on_stop is called when the TaskSet is stopping """
    #     self.logout()



    # @task(2)
    # def index(self):
    #     self.client.get("/")

    # @task(1)
    # def profile(self):
    #     self.client.get("/profile")

    # def login(self):
    #     self.client.post("/login", {"username":"ellen_key", "password":"education"})

    # def logout(self):
    #     self.client.post("/logout", {"username":"ellen_key", "password":"education"})

    # def get_ancestors(self):
    #     self.client.get("/ancestors/MONDO%3A0004634")
    # the above is fine, classic python definition style... or we can use decorators, in a functionally symmetric way, below...