import requests
import random
import string
import pytz
import allure

from faker import Faker


@allure.step("Генерируем случайные данные для курьера")
def generate_random_courier_data():
    def generate_random_string(length):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for _ in range(length))

    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    return {
        "login": login,
        "password": password,
        "firstName": first_name
    }


@allure.step("Регистрируем курьера")
def register_new_courier_and_return_login_password():
    courier_data = generate_random_courier_data()

    response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=courier_data)

    if response.status_code == 201:
        return [courier_data['login'], courier_data['password'], courier_data['firstName']]
    else:
        return None


@allure.step("Генерируем данные для пользовательского заказа, не включая цвет")
def generate_order_data():
    faker = Faker('ru_RU')
    first_name = faker.first_name()
    last_name = faker.last_name()
    address = faker.street_address()
    metro_station = random.randint(1, 20)
    phone = str(random.randint(10000000000, 99000000000))
    random_datetime = faker.date_time_this_century()
    formatted_datetime = random_datetime.astimezone(pytz.utc).strftime('%Y-%m-%dT%H:%M:%S.000Z')
    rent_time = random.randint(1, 7)
    comment = faker.text(15)

    return {
        "firstName": first_name,
        "lastName": last_name,
        "address": address,
        "metroStation": metro_station,
        "phone": phone,
        "rentTime": rent_time,
        "deliveryDate": formatted_datetime,
        "comment": comment
        }

