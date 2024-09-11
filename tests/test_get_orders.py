import requests
import allure

from data.data_orders import CreateOrder as order_data


class TestGetOrders:

    @allure.description("Вызываем метод /api/v1/orders и проверяем, что он содержит заказы")
    def test_get_orders(self):
        response = requests.get(url=order_data.url)
        assert "order", "createdAt" == response.json()

