class CreateCourierData:
    path = "https://qa-scooter.praktikum-services.ru"
    method = "/api/v1/courier"
    url = path + method

    existing_user = {
        "login": "wukongTheMonkey",
        "password": "banana123",
        "firstName": "StoneMonkey"
    }

    not_enough_data_error = '{"code":400,"message":"Недостаточно данных для создания учетной записи"}'
    same_login_error = '{"code":409,"message":"Этот логин уже используется. Попробуйте другой."}'
