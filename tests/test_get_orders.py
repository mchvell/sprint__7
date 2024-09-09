import requests
import allure

from data.data_get_orders import DataGetOrders as data_orders


class TestGetOrders:

    @allure.description("Вызываем метод /api/v1/orders и проверяем, что он содержит заказы")
    def test_get_orders(self):
        response = requests.get(url=data_orders.url)
        assert "order", "createdAt" == response.json()

