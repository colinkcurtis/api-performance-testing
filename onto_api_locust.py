from locust import HttpLocust, TaskSet, task

class UserBehavior(TaskSet):
    #1
    @task(1)
    def get_children(self):
        self.client.get("/children/MONDO%3A0004634")
    #2
    # @task(1) #the values inside the parantheses give a relative weight to the frequency of execution of each task by the locust-swarm!
    # def get_all_properties_0(self):
    #     self.client.get("/all_properties/CHEBI:89671")
    # #3
    # @task(1)
    # def get_all_properties_1(self):
    #     self.client.get("/all_properties/CHEBI:88883")
    # #4
    # @task(1)
    # def get_all_properties_2(self):
    #     self.client.get("/all_properties/CHEBI:89319")
    # #5
    # @task(1)
    # def get_all_properties_3(self):
    #     self.client.get("/all_properties/CHEBI:89806")
    # #6
    # @task(1)
    # def get_all_properties_4(self):
    #     self.client.get("/all_properties/CHEBI:88923")
    # #7
    # @task(1)
    # def get_all_properties_5(self):
    #     self.client.get("/all_properties/CHEBI:88754")
    # #8
    # @task(1)
    # def get_all_properties_6(self):
    #     self.client.get("/all_properties/CHEBI:89407")
    # #9
    # @task(1)
    # def get_all_properties_7(self):
    #     self.client.get("/all_properties/CHEBI:88740")
    # #10
    # @task(1)
    # def get_all_properties_8(self):
    #     self.client.get("/all_properties/CHEBI:88855")
    # #11
    # @task(1)
    # def get_all_properties_9(self):
    #     self.client.get("/all_properties/CHEBI:89326")
    # #12
    # @task(1)
    # def get_all_properties_10(self):
    #     self.client.get("/all_properties/CHEBI:89067")
    # #13
    # @task(1)
    # def get_all_properties_11(self):
    #     self.client.get("/all_properties/CHEBI:88856")
    # #14
    # @task(1)
    # def get_all_properties_12(self):
    #     self.client.get("/all_properties/CHEBI:88753")
    # #15
    # @task(1)
    # def get_all_properties_13(self):
    #     self.client.get("/all_properties/CHEBI:88755")
    # #16
    # @task(1)
    # def get_all_properties_14(self):
    #     self.client.get("/all_properties/CHEBI:88869")
    # #17
    # @task(1)
    # def get_all_properties_15(self):
    #     self.client.get("/all_properties/CHEBI:88758")
    # #18
    # @task(1)
    # def get_all_properties_16(self):
    #     self.client.get("/all_properties/CHEBI:88737")
    # #19
    # @task(1)
    # def get_all_properties_17(self):
    #     self.client.get("/all_properties/CHEBI:89402")
    # #20
    # @task(1)
    # def get_all_properties_18(self):
    #     self.client.get("/all_properties/CHEBI:88731")
    # #21
    # @task(1)
    # def get_all_properties_19(self):
    #     self.client.get("/all_properties/CHEBI:86210")
    # #22
    # @task(1)
    # def get_all_properties_20(self):
    #     self.client.get("/all_properties/CHEBI:88909")
    # #23
    # @task(1)
    # def get_all_properties_21(self):
    #     self.client.get("/all_properties/CHEBI:88895")
    # #24
    # @task(1)
    # def get_all_properties_22(self):
    #     self.client.get("/all_properties/CHEBI:89326")

    


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 0
    max_wait = 1000