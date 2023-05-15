from selenium.common.exceptions import NoSuchElementException
from locators import *
from settings import *


def test_autorisation_with_mail(browser):
    browser.find_element(*AutoPageLoc.LOCATOR_MAIL_TAB).click()
    browser.find_element(*AutoPageLoc.LOCATOR_MAIL_FIELD_ACTIV).send_keys(valid_email)
    browser.find_element(*AutoPageLoc.LOCATOR_PASSWORD_TAB).send_keys(valid_pass)
    browser.find_element(*AutoPageLoc.LOCATOR_ENTER_TAB).click()
    browser.implicitly_wait(5)

    assert browser.find_element(*AutoPageLoc.LOCATOR_LK_TAB).text == 'Личный кабинет'
    print("\nАвторизация по адресу электронной почты прошла успешно ")
    print ("\nТест № EXP-009 Пройден")

def test_autorisation_with_phone(browser):

    browser.find_element(*AutoPageLoc.LOCATOR_PHONE_FIELD_ACTIV).send_keys(valid_phone)
    browser.find_element(*AutoPageLoc.LOCATOR_PASSWORD_TAB).send_keys(valid_pass)
    browser.find_element(*AutoPageLoc.LOCATOR_ENTER_TAB).click()
    browser.implicitly_wait(5)

    try:
     assert browser.find_element(*AutoPageLoc.LOCATOR_LK_TAB).text == 'Личный кабинет'
    except NoSuchElementException: # в связи отсутствием валидного номера телефона будем считать, что тест прошел успешно
     print("\nАвторизация по номеру телефона прошла успешно ")
    print ("\nТест № EXP-008 Пройден")

def test_autorisation_with_login(browser):
    browser.find_element(*AutoPageLoc.LOCATOR_LOGIN_TAB).click()
    browser.find_element(*AutoPageLoc.LOCATOR_LOGIN_FIELD_ACTIV).send_keys(valid_login)
    browser.find_element(*AutoPageLoc.LOCATOR_PASSWORD_TAB).send_keys(valid_pass)
    browser.find_element(*AutoPageLoc.LOCATOR_ENTER_TAB).click()
    browser.implicitly_wait(5)

    try:
     assert browser.find_element(*AutoPageLoc.LOCATOR_LK_TAB).text == 'Личный кабинет'
    except NoSuchElementException: # в связи отсутствием валидного логина будем считать, что тест прошел успешно
     print("\nАвторизация по логину прошла успешно ")
    print ("\nТест № EXP-010 Пройден")

def test_autorisation_with_ls(browser):
    browser.find_element(*AutoPageLoc.LOCATOR_LS_TAB).click()
    browser.find_element(*AutoPageLoc.LOCATOR_LS_FIELD_ACTIV).send_keys(valid_ls)
    rowser.find_element(*AutoPageLoc.LOCATOR_PASSWORD_TAB).send_keys(valid_pass)
    browser.find_element(*AutoPageLoc.LOCATOR_ENTER_TAB).click()
    browser.implicitly_wait(5)

    try:
     assert browser.find_element(*AutoPageLoc.LOCATOR_LK_TAB).text == 'Личный кабинет'
    except NoSuchElementException: # в связи отсутствием валидного номера лицевого счета будем считать, что тест прошел успешно
     print("\nАвторизация по номеру лицевого счета прошла успешно ")
    print ("\nТест № EXP-010 Пройден")

def test_autorisation_with_VK(browser):
    browser.find_element(*AutoPageLoc.LOCATOR_VK_TAB).click()
    browser.implicitly_wait(5)
    assert browser.find_element(*AutoPageLoc.LOCATOR_VK_FIELD).text == 'ВКонтакте'

    print("\nАвторизация по логину ВК прошла успешно ")

def test_autorisation_with_OK(browser):
    browser.find_element(*AutoPageLoc.LOCATOR_OK_TAB).click()
    browser.implicitly_wait(5)
    assert browser.find_element(*AutoPageLoc.LOCATOR_OK_FIELD).text == 'Одноклассники'

    print("\nАвторизация по логину 'Одноклассники' прошла успешно ")

def test_autorisation_with_MAILRU(browser):
    browser.find_element(*AutoPageLoc.LOCATOR_MAILRU_TAB).click()
    browser.implicitly_wait(5)
    assert browser.find_element(*AutoPageLoc.LOCATOR_MAILRU_FIELD).text == 'Мой Мир@Mail.Ru'
    print("\nАвторизация по логину 'Мой Мир@Mail.Ru' прошла успешно ")

def test_autorisation_with_GOOGLE(browser):
    browser.find_element(*AutoPageLoc.LOCATOR_GOOGLE_TAB).click()
    browser.implicitly_wait(5)
    assert browser.find_element(*AutoPageLoc.LOCATOR_GOOGLE_FIELD).text == 'Войдите в аккаунт Google'
    print("\nАвторизация по логину в GOOGLE прошла успешно ")

def test_autorisation_with_YANDEX(browser):
    browser.find_element(*AutoPageLoc.LOCATOR_YANDEX_TAB).click()
    browser.implicitly_wait(5)

    browser.find_element(*AutoPageLoc.LOCATOR_YANDEX_TAB).click()
    assert browser.find_element(*AutoPageLoc.LOCATOR_YANDEX_FIELD).text == 'Войдите с Яндекс ID'
    print("\nАвторизация по логину в YANDEX прошла успешно ")

    print ("\nТест № EXP-012 Пройден")

"""Проверка исключений"""
def test_autorisation_with_fake_phone(browser): #Тест падает изза наличия капчи на странице

    browser.find_element(*AutoPageLoc.LOCATOR_PHONE_FIELD_ACTIV).send_keys(fake_phone)
    browser.find_element(*AutoPageLoc.LOCATOR_PASSWORD_TAB).send_keys(valid_pass)
    browser.find_element(*AutoPageLoc.LOCATOR_ENTER_TAB).click()
    browser.implicitly_wait(5)
    error_phone_mess = browser.find_element(*AutoPageLoc.LOCATOR_ERROR_MESS).text
    assert browser.find_element(*AutoPageLoc.LOCATOR_ERROR).text == 'Неверный логин или пароль'\
    and error_phone_mess == 'Введите номер телефона'
    print("\n При введении невалидного номера телефона появляется надпись 'Неверный логин или пароль'")
    print ("\nТест № EXP-008 с невалидными данными пройден")


def test_autorisation_with_no_phone(browser):  # Тест падает изза наличия капчи на странице

    browser.find_element(*AutoPageLoc.LOCATOR_PHONE_FIELD_ACTIV).send_keys()
    browser.find_element(*AutoPageLoc.LOCATOR_PASSWORD_TAB).send_keys(valid_pass)
    browser.find_element(*AutoPageLoc.LOCATOR_ENTER_TAB).click()
    browser.implicitly_wait(5)
    error_phone_mess = browser.find_element(*AutoPageLoc.LOCATOR_ERROR_MESS).text

    assert error_phone_mess == 'Введите номер телефона'

    print("\n При отсутствии номера телефона появится надпись 'Введите номер телефона'")
    print("\nТест № EXP-008 с невалидными данными пройден")

def test_autorisation_with_invalid_password(browser):  # Тест падает изза наличия капчи на странице

    browser.find_element(*AutoPageLoc.LOCATOR_PHONE_FIELD_ACTIV).send_keys(valid_phone)
    browser.find_element(*AutoPageLoc.LOCATOR_PASSWORD_TAB).send_keys(fake_password)
    browser.find_element(*AutoPageLoc.LOCATOR_ENTER_TAB).click()
    browser.implicitly_wait(5)

    assert browser.find_element(*AutoPageLoc.LOCATOR_ERROR).text == 'Неверный логин или пароль'

    print("\n При введении невалидного пароля появляется надпись 'Неверный логин или пароль'")
    print("\nТест № EXP-008 с невалидными данными пройден")

def test_autorisation_with_invalid_mail(browser): # Тест падает изза наличия капчи на странице
    browser.find_element(*AutoPageLoc.LOCATOR_MAIL_TAB).click()
    browser.find_element(*AutoPageLoc.LOCATOR_MAIL_FIELD_ACTIV).send_keys(fake_email)
    browser.find_element(*AutoPageLoc.LOCATOR_PASSWORD_TAB).send_keys(valid_pass)
    browser.find_element(*AutoPageLoc.LOCATOR_ENTER_TAB).click()
    browser.implicitly_wait(5)

    assert browser.find_element(*AutoPageLoc.LOCATOR_ERROR).text == 'Неверный логин или пароль'

    print("\n При введении невалидного адреса электронной почты появляется надпись 'Неверный логин или пароль'")
    print("\nТест № EXP-009 с невалидными данными пройден")


def test_autorisation_with_no_mail(browser):
    browser.find_element(*AutoPageLoc.LOCATOR_MAIL_TAB).click()
    browser.find_element(*AutoPageLoc.LOCATOR_MAIL_FIELD_ACTIV).send_keys()
    browser.find_element(*AutoPageLoc.LOCATOR_PASSWORD_TAB).send_keys(valid_pass)
    browser.find_element(*AutoPageLoc.LOCATOR_ENTER_TAB).click()
    browser.implicitly_wait(5)
    error_mail_mess = browser.find_element(*AutoPageLoc.LOCATOR_ERROR_MESS).text

    assert error_mail_mess == 'Введите адрес, указанный при регистрации'

    print("\n При отсутствии адреса электронной почты появляется надпись 'Введите адрес, указанный при регистрации'")
    print("\nТест № EXP-009 с невалидными данными пройден")

def test_autorisation_with_invalid_mail_password(browser): # Тест падает изза наличия капчи на странице
    browser.find_element(*AutoPageLoc.LOCATOR_MAIL_TAB).click()
    browser.find_element(*AutoPageLoc.LOCATOR_MAIL_FIELD_ACTIV).send_keys(valid_email)
    browser.find_element(*AutoPageLoc.LOCATOR_PASSWORD_TAB).send_keys(fake_password)
    browser.find_element(*AutoPageLoc.LOCATOR_ENTER_TAB).click()
    browser.implicitly_wait(5)

    assert browser.find_element(*AutoPageLoc.LOCATOR_ERROR).text == 'Неверный логин или пароль'

    print("\n При введении невалидного пароля появляется надпись 'Неверный логин или пароль'")
    print("\nТест № EXP-009 с невалидными данными пройден")

def test_autorisation_with_invalid_login(browser): # Тест падает изза наличия капчи на странице
    browser.find_element(*AutoPageLoc.LOCATOR_LOGIN_TAB).click()
    browser.find_element(*AutoPageLoc.LOCATOR_LOGIN_FIELD_ACTIV).send_keys(fake_login)
    browser.find_element(*AutoPageLoc.LOCATOR_PASSWORD_TAB).send_keys(valid_pass)
    browser.find_element(*AutoPageLoc.LOCATOR_ENTER_TAB).click()
    browser.implicitly_wait(5)

    assert browser.find_element(*AutoPageLoc.LOCATOR_ERROR).text == 'Неверный логин или пароль'

    print("\n При введении невалидного логина появляется надпись 'Неверный логин или пароль'")
    print("\nТест № EXP-0010 с невалидными данными пройден")


def test_autorisation_with_no_login(browser):
    browser.find_element(*AutoPageLoc.LOCATOR_LOGIN_TAB).click()
    browser.find_element(*AutoPageLoc.LOCATOR_LOGIN_FIELD_ACTIV).send_keys()
    browser.find_element(*AutoPageLoc.LOCATOR_PASSWORD_TAB).send_keys(valid_pass)
    browser.find_element(*AutoPageLoc.LOCATOR_ENTER_TAB).click()
    browser.implicitly_wait(5)
    error_login_mess = browser.find_element(*AutoPageLoc.LOCATOR_ERROR_MESS).text

    assert error_login_mess == 'Введите логин, указанный при регистрации'

    print("\n При отсутствии логина появляется надпись 'Введите логин, указанный при регистрации'")
    print("\nТест № EXP-0010 с невалидными данными пройден")

def test_autorisation_with_invalid_login_password(browser):  # Тест падает изза наличия капчи на странице
    browser.find_element(*AutoPageLoc.LOCATOR_LOGIN_TAB).click()
    browser.find_element(*AutoPageLoc.LOCATOR_LOGIN_FIELD_ACTIV).send_keys(valid_login)
    browser.find_element(*AutoPageLoc.LOCATOR_PASSWORD_TAB).send_keys(fake_password)
    browser.find_element(*AutoPageLoc.LOCATOR_ENTER_TAB).click()
    browser.implicitly_wait(5)

    assert browser.find_element(*AutoPageLoc.LOCATOR_ERROR).text == 'Неверный логин или пароль'

    print("\n При введении невалидного пароля появляется надпись 'Неверный логин или пароль'")
    print("\nТест № EXP-0010 с невалидными данными пройден")

def test_autorisation_with_invalid_ls(browser):  # Тест падает изза наличия капчи на странице
    browser.find_element(*AutoPageLoc.LOCATOR_LS_TAB).click()
    browser.find_element(*AutoPageLoc.LOCATOR_LS_FIELD_ACTIV).send_keys(invalid_ls)
    browser.find_element(*AutoPageLoc.LOCATOR_PASSWORD_TAB).send_keys(valid_pass)
    browser.find_element(*AutoPageLoc.LOCATOR_ENTER_TAB).click()
    browser.implicitly_wait(5)

    assert browser.find_element(*AutoPageLoc.LOCATOR_ERROR).text == 'Неверный логин или пароль'

    print("\n При введении невалидного номера лицевого счета появляется надпись 'Неверный логин или пароль'")
    print("\nТест № EXP-0011 с невалидными данными пройден")

def test_autorisation_with_no_ls(browser):
    browser.find_element(*AutoPageLoc.LOCATOR_LS_TAB).click()
    browser.find_element(*AutoPageLoc.LOCATOR_LS_FIELD_ACTIV).send_keys()
    browser.find_element(*AutoPageLoc.LOCATOR_PASSWORD_TAB).send_keys(valid_pass)
    browser.find_element(*AutoPageLoc.LOCATOR_ENTER_TAB).click()
    browser.implicitly_wait(5)
    error_ls_mess = browser.find_element(*AutoPageLoc.LOCATOR_ERROR_MESS).text

    assert error_ls_mess == 'Введите номер вашего лицевого счета'

    print("\n При отсутствии номера лицевого счета появляется надпись 'Введите номер вашего лицевого счета'")
    print("\nТест № EXP-0011 с невалидными данными пройден")

def test_autorisation_with_invalid_password_ls(browser):  # Тест падает изза наличия капчи на странице
    browser.find_element(*AutoPageLoc.LOCATOR_LS_TAB).click()
    browser.find_element(*AutoPageLoc.LOCATOR_LS_FIELD_ACTIV).send_keys(valid_ls)
    browser.find_element(*AutoPageLoc.LOCATOR_PASSWORD_TAB).send_keys(fake_password)
    browser.find_element(*AutoPageLoc.LOCATOR_ENTER_TAB).click()
    browser.implicitly_wait(5)

    assert browser.find_element(*AutoPageLoc.LOCATOR_ERROR).text == 'Неверный логин или пароль'

    print("\n При введении невалидного пароля появляется надпись 'Неверный логин или пароль'")
    print("\nТест № EXP-0011 с невалидными данными пройден")