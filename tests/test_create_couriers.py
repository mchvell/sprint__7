import requests
import allure

from user_generator import register_new_courier_and_return_login_password as create_new_user
from user_generator import generate_random_courier_data as data_generator


class TestCreatingCourier:
    path = "https://qa-scooter.praktikum-services.ru"
    method = "/api/v1/courier"

    @allure.description("Вызываем метод /api/v1/courier и проверяем, что стандартный метод возвращает валидный список")
    def test_create_new_courier(self):
        new_user_credentials = create_new_user()
        assert len(new_user_credentials) == 3

    @allure.description("Вызываем метод /api/v1/courier и проверяем, нельзя создать нового курьера на существующие креды")
    def test_create_courier_with_existing_data(self):
        payload = {
            "login": "wukongTheMonkey",
            "password": "banana123",
            "firstName": "StoneMonkey"
        }
        response = requests.post(url=self.path + self.method, data=payload)
        assert response.status_code == 201

    @allure.description("Вызываем метод /api/v1/courier и проверяем, что нельзя создать курьера с пустым полем")
    def test_create_new_user_with_empty_field(self):
        payload = {
            "login": "wukongTheMonkey",
            "password": "banana123",
            "firstName": ""

        }
        response = requests.post(url=self.path + self.method, data=payload)
        assert response.status_code != 201

    @allure.description("Вызываем метод /api/v1/courier и проверяем, что ручка отдает валидный ответ")
    def test_create_new_courier_text_check(self):
        payload = data_generator()
        response = requests.post(url=self.path + self.method, data=payload)
        text = {'ok': True}
        assert response.json() == text

    @allure.description("Вызываем метод /api/v1/courier и проверяем, что нельзя создать курьера без одного из полей")
    def test_create_new_user_without__field(self):
        payload = {
            "password": "banana123",
            "firstName": "StoneMonkey"

        }
        response = requests.post(url=self.path + self.method, data=payload)
        error_text = '{"code":400,"message":"Недостаточно данных для создания учетной записи"}'

        assert response.text == error_text

    @allure.description("Вызываем метод /api/v1/courier и проверяем, что при повторе данных ручка отдает валидный ответ")
    def test_create_new_user_with_existing_data_return_error(self):
        payload = {
            "login": "wukongTheMonkey",
            "password": "banana123",
            "firstName": "StoneMonkey"

        }
        response = requests.post(url=self.path + self.method, data=payload)
        error_text = '{"code":409,"message":"Этот логин уже используется. Попробуйте другой."}'
        assert response.text == error_text
