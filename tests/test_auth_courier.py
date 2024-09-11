import requests
import allure

from user_generator import register_new_courier_and_return_login_password as create_new_user
from user_generator import generate_random_courier_data as data_generator
from data.data_auth import AuthData as auth_data


class TestCourierAuth:
    @allure.description("Вызываем метод /api/v1/courier/login и проверяем успешную авторизацию")
    def test_auth_success(self):
        user_data = create_new_user()
        payload = {"login": user_data[0], "password": user_data[1]}

        response = requests.post(url=auth_data.url, data=payload)
        valid_status_code = 200
        assert response.status_code == valid_status_code

        # добавлена вторая проверка на тело заказа
        json_data = response.json()
        assert "id" in json_data

    @allure.description("Вызываем метод /api/v1/courier/login и передаем в него пустое поле пароль")
    def test_auth_without_one_empty_field(self):
        user_data = create_new_user()
        payload = {"login": user_data[0], "password": ""}

        response = requests.post(url=auth_data.url, data=payload)
        error_status_code = 400
        assert response.status_code == error_status_code

        # добавлена вторая проверка на контент боди ответа
        assert response.text == auth_data.not_enough_data

    @allure.description("Вызываем метод /api/v1/courier/login и не передаем в него поле пароль")
    def test_auth_without_one_field(self):
        user_data = create_new_user()
        payload = {"login": user_data[0]}

        response = requests.post(url=auth_data.url, data=payload)
        error_status_code = 504
        assert response.status_code == error_status_code

    @allure.description("Вызываем метод /api/v1/courier/login и не передаем в него несуществующие креды")
    def test_auth_with_non_existing_user(self):
        user_data = list(data_generator())
        payload = {"login": user_data[0], "password": user_data[1]}

        response = requests.post(url=auth_data.url, data=payload)
        assert response.text == auth_data.profile_not_found_error


