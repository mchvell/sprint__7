from settings import BaseUrl as b


class CreateCourierData:
    method = "/api/v1/courier"
    url = b.base_url + method

    existing_user = {
        "login": "wukongTheMonkey",
        "password": "banana123",
        "firstName": "StoneMonkey"
    }

    not_enough_data_error = '{"code":400,"message":"Недостаточно данных для создания учетной записи"}'
    same_login_error = '{"code":409,"message":"Этот логин уже используется. Попробуйте другой."}'
