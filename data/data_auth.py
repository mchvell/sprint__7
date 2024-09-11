from settings import BaseUrl as b


class AuthData:
    method = "/api/v1/courier/login"
    url = b.base_url + method
    profile_not_found_error = '{"code":404,"message":"Учетная запись не найдена"}'
    not_enough_data = '{"code":400,"message":"Недостаточно данных для входа"}'

