import requests
import allure

from user_generator import register_new_courier_and_return_login_password as create_new_user
from user_generator import generate_random_courier_data as data_generator


class TestCourierAuth:
    path = "https://qa-scooter.praktikum-services.ru"
    method = "/api/v1/courier/login"

    @allure.description("Вызываем метод /api/v1/courier/login и проверяем успешную авторизацию")
    def test_auth_success(self):
        user_data = create_new_user()
        payload = {"login": user_data[0], "password": user_data[1]}

        response = requests.post(url=self.path+self.method, data=payload)
        valid_status_code = 200
        assert response.status_code == valid_status_code

    @allure.description("Вызываем метод /api/v1/courier/login и передаем в него пустое поле пароль")
    def test_auth_without_one_empty_field(self):
        user_data = create_new_user()
        payload = {"login": user_data[0], "password": ""}

        response = requests.post(url=self.path+self.method, data=payload)
        error_status_code = 400
        assert response.status_code == error_status_code

    @allure.description("Вызываем метод /api/v1/courier/login и не передаем в него поле пароль")
    def test_auth_without_one_field(self):
        user_data = create_new_user()
        payload = {"login": user_data[0]}

        response = requests.post(url=self.path+self.method, data=payload)
        error_status_code = 504
        assert response.status_code == error_status_code

    @allure.description("Вызываем метод /api/v1/courier/login и не передаем в него несуществующие креды")
    def test_auth_with_non_existing_user(self):
        user_data = list(data_generator())
        payload = {"login": user_data[0], "password": user_data[1]}

        response = requests.post(url=self.path+self.method, data=payload)
        error_text = '{"code":404,"message":"Учетная запись не найдена"}'
        assert response.text == error_text

    @allure.description("Вызываем метод /api/v1/courier/login и проверяем, что получаем в ответе id")
    def test_auth_success_id(self):
        user_data = create_new_user()
        payload = {"login": user_data[0], "password": user_data[1]}

        response = requests.post(url=self.path+self.method, data=payload)
        json_data = response.json()
        assert "id" in json_data
