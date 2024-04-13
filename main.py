from locust import HttpUser, between, task


class WebsiteUser(HttpUser):
    wait_time = between(5, 15)

    @task
    def post_user_Create(self):
        payload = {
            "id": 436732471,
            "username": "TestBerke123",
            "firstName": "Berke",
            "lastName": "Yorulmaz",
            "email": "testberke@test.com",
            "password": "123",
            "phone": "543437831",
            "userStatus": 1
            }
        self.client.post("/v2/user", json=payload)

    @task
    def get_user_info(self):
        self.client.get("/v2/user/TestBerke123")

    @task
    def get_user_login(self):
        payload = {
            "username": "TestBerke123",
            "password": "123"
            }
        self.client.get("/v2/user/login", params=payload)

    @task
    def get_user_logout(self):
        self.client.get("/v2/user/logout")

    # @task
    # def delete_user(self):
    #     payload = {
    #         "id": 4367317471,
    #         "username": "TestBerke1234",
    #         "firstName": "Berkesdfsd",
    #         "lastName": "Yorulmazdsf",
    #         "email": "testberke2@test.com",
    #         "password": "123",
    #         "phone": "5437322831",
    #         "userStatus": 1
    #         }
    #     self.client.post("/v2/user", json=payload)
    #     self.client.delete("/v2/user/TestBerke1234")

    @task
    def post_create_with_array(self):
        payload = {
            "id": 745638023,
            "username": "jdksdbgdj",
            "firstName": "sgdsdgdsasg",
            "lastName": "dsgsgdfh",
            "email": "djghdsjgal@fdhgjd.com",
            "password": "123",
            "phone": "7452359230",
            "userStatus": 0
            }
        self.client.post("/v2/user/createWithArray", json=payload)

