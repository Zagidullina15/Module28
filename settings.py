from faker import Faker

import string

"""Данные для авторизации в системе"""
valid_firstname = 'Иван'
valid_lastname = 'Иванов'
valid_email = 'IvanIvanovAltay@yandex.ru'
valid_pass = 'SkF.INQAP-1034'
valid_phone = '+79201111111'
valid_login = 'Ivan-Ivanov'
valid_ls = '111111111111'
from locators import AutoPageLoc
"""Фейковые данные для авторизации в системе"""
# ввод данных на русском языке
fake_ru = Faker('ru_RU')
fake_firstname = fake_ru.first_name()
fake_lastname = fake_ru.last_name()
fake_phone = fake_ru.phone_number()
#ввод данных на английском языке
fake = Faker()
fake_firstname_en = fake.first_name()
fake_lastname_en = fake.last_name()
fake_password = fake.password()
fake_email = fake.email()
fake_login = fake.user_name()
invalid_ls = '211111111111'
region = 'Алтайский край'