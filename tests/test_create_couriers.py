import requests
import allure

from user_generator import register_new_courier_and_return_login_password as create_new_user
from user_generator import generate_random_courier_data as data_generator
from data.data_create_courier import CreateCourierData as courier_data


class TestCreatingCourier:

    @allure.description("Вызываем метод /api/v1/courier и проверяем, что стандартный метод возвращает валидный список")
    def test_create_new_courier(self):
        new_user_credentials = create_new_user()
        assert len(new_user_credentials) == 3

    @allure.description("Вызываем метод /api/v1/courier и проверяем, нельзя создать нового курьера на существующие креды")
    def test_create_courier_with_existing_data(self):
        payload = courier_data.existing_user
        response = requests.post(url=courier_data.url, data=payload)
        assert response.status_code != 201

        # добавлена вторая проверка на контент боди
        assert response.text == courier_data.same_login_error

    @allure.description("Вызываем метод /api/v1/courier и проверяем, что нельзя создать курьера с пустым полем")
    def test_create_new_user_with_empty_field(self):
        payload = {
            "login": "",
            "password": "banana123",
            "firstName": ""

        }
        response = requests.post(url=courier_data.url, data=payload)
        assert response.text == courier_data.not_enough_data_error

    @allure.description("Вызываем метод /api/v1/courier и проверяем, что ручка отдает валидный ответ")
    def test_create_new_courier_text_check(self):
        payload = data_generator()
        response = requests.post(url=courier_data.url, data=payload)
        text = {'ok': True}
        assert response.json() == text

    @allure.description("Вызываем метод /api/v1/courier и проверяем, что при повторе данных ручка отдает валидный ответ")
    def test_create_new_user_with_existing_data_return_error(self):
        payload = courier_data.existing_user
        response = requests.post(url=courier_data.url, data=payload)
        error_text = courier_data.same_login_error
        assert response.text == error_text
