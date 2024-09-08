import requests
import allure

from user_generator import generate_order_data


class TestGetOrders:
    path = "https://qa-scooter.praktikum-services.ru"
    method = "/api/v1/orders"

    @allure.description("Вызываем метод /api/v1/orders и проверяем, что он содержит заказы")
    def test_get_orders(self):
        response = requests.get(url=self.path+self.method)
        assert "order", "createdAt" == response.json()

