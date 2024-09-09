import json

import pytest
import requests
import allure

from user_generator import generate_order_data
from data.data_create_order import CreateOrder as orders_data


class TestChooseColors:

    @allure.description("Вызываем метод /api/v1/orders и не передаем в него через парамы цвета, а также проверяем что заказ создан")
    @pytest.mark.parametrize("color", orders_data.colours)
    def test_create_order_with_one_color(self, color):
        order_data = generate_order_data()
        order_data["color"] = color
        payload = json.dumps(order_data)
        response = requests.post(url=orders_data.url, data=payload)
        assert response.status_code == 201

    @allure.description("Вызываем метод /api/v1/orders и передаем в него оба цвета, а также проверяем что заказ создан")
    def test_create_order_with_both_colours(self):
        order_data = generate_order_data()
        order_data["color"] = orders_data.colours
        payload = json.dumps(order_data)
        response = requests.post(url=orders_data.url, data=payload)
        assert response.status_code == 201

    @allure.description("Вызываем метод /api/v1/orders и не передаем в него цвета, а также проверяем что заказ создан")
    def test_create_order_without_colour(self):
        payload = generate_order_data()
        response = requests.post(url=orders_data.url, data=payload)
        assert response.status_code == 201

    @allure.description("Вызываем метод /api/v1/orders и проверяем, что получаем валидный ответ от сервера")
    def test_create_order_response_body(self):
        payload = generate_order_data()
        response = requests.post(url=orders_data.url, data=payload)
        assert "track" in response.json()


