from locust import HttpLocust, TaskSet, task


class UserBehavior(TaskSet):
    @task(2)
    def profile(self):
        a = self.client.get("http://tpvote.com/api/activity/home").text
        print(a)
class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    host = ''
    min_wait = 0
    max_wait = 0
