from settings import BaseUrl as b


class CreateOrder:
    method = "/api/v1/orders"
    url = b.base_url + method
    colours = ["BLACK", "GREY"]