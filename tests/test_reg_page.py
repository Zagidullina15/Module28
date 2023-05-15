from locators import *
from settings import *
import pytest

def test_reg_page(browser):
    browser.find_element(*AutoPageLoc.LOCATOR_REG_TAB).click()
    assert browser.find_element(*RegPageLoc.LOCATOR_REG_FIELD).text == 'Регистрация'
    print("\nПереход на страницу регистрации прошел успешно ")
    print("\nТест № EXP-016 Пройден")

def test_reg_page_registration(browser_reg_page):

    input_field = browser_reg_page.find_elements(*RegPageLoc.LOCATOR_INPUT_FIELD)
    input_field[0].send_keys(fake_firstname)
    input_field[1].send_keys(fake_lastname)
    input_field[3].send_keys(fake_email)
    input_field[4].send_keys(fake_password)
    input_field[5].send_keys(fake_password)
    browser_reg_page.find_element(*RegPageLoc.LOCATOR_BUTTON_REGISTRATION).click()

    assert browser_reg_page.find_element(*RegPageLoc.LOCATOR_REGISTRATION_CODE_FIELD).text == 'Подтверждение email'
    print("\nПереход на страницу получения кода подтверждения прошел успешно ")
    print("\nТест № EXP-018 Пройден")

def test_reg_page_no_data(browser_reg_page):
    input_field = browser_reg_page.find_elements(*RegPageLoc.LOCATOR_INPUT_FIELD)
    input_field[0].send_keys()
    input_field[1].send_keys()
    input_field[3].send_keys()
    input_field[4].send_keys()
    input_field[5].send_keys()
    browser_reg_page.find_element(*RegPageLoc.LOCATOR_BUTTON_REGISTRATION).click()
    error_message = browser_reg_page.find_elements(*RegPageLoc.LOCATOR_ERROR_MESS)
    name_error_message = error_message[0]
    last_name_error_message = error_message[0]
    mail_error_message = error_message[2]
    password_error_message = error_message[3]
    password_confirm_error_message = error_message[4]
    assert name_error_message.text == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'\
    and last_name_error_message.text == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.' \
    and mail_error_message.text == 'Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru' \
    and password_error_message.text == 'Длина пароля должна быть не менее 8 символов' \
    and password_confirm_error_message.text == 'Длина пароля должна быть не менее 8 символов'
    print("\n Появились сообщения об ошибке регистрации ")
    print("\nТест № EXP-018 Пройден")

def test_reg_page_allready_reg(browser_reg_page):

    input_field = browser_reg_page.find_elements(*RegPageLoc.LOCATOR_INPUT_FIELD)
    input_field[0].send_keys(valid_firstname)
    input_field[1].send_keys(valid_lastname)
    input_field[3].send_keys(valid_email)
    input_field[4].send_keys(valid_pass)
    input_field[5].send_keys(valid_pass)
    browser_reg_page.find_element(*RegPageLoc.LOCATOR_BUTTON_REGISTRATION).click()

    assert browser_reg_page.find_element(*RegPageLoc.LOCATOR_REGISTRATION_CODE_FIELD).text == 'Регистрация'
    print("\nПоявилась форма, сообщающая о том, что пользователь уже зарегистрирован ")
    print("\nТест № EXP-018 Пройден")

def test_reg_page_invalid_name_en(browser_reg_page):
    input_field = browser_reg_page.find_elements(*RegPageLoc.LOCATOR_INPUT_FIELD)
    input_field[0].send_keys(fake_firstname_en)
    input_field[1].send_keys(fake_lastname)
    input_field[3].send_keys(fake_email)
    input_field[4].send_keys(fake_password)
    input_field[5].send_keys(fake_password)
    browser_reg_page.find_element(*RegPageLoc.LOCATOR_BUTTON_REGISTRATION).click()
    error_message = browser_reg_page.find_elements(*RegPageLoc.LOCATOR_ERROR_MESS)
    name_error_message = error_message[0]


    assert name_error_message.text == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'

    print("\n Появилось сообщение об ошибке ввода имени ")
    print("\nТест № EXP-019 Пройден")

def test_reg_page_invalid_name_short(browser_reg_page):
    input_field = browser_reg_page.find_elements(*RegPageLoc.LOCATOR_INPUT_FIELD)
    input_field[0].send_keys('д')
    input_field[1].send_keys(fake_lastname)
    input_field[3].send_keys(fake_email)
    input_field[4].send_keys(fake_password)
    input_field[5].send_keys(fake_password)
    browser_reg_page.find_element(*RegPageLoc.LOCATOR_BUTTON_REGISTRATION).click()
    error_message = browser_reg_page.find_elements(*RegPageLoc.LOCATOR_ERROR_MESS)
    name_error_message = error_message[0]

    assert name_error_message.text == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'

    print("\n Появилось сообщение об ошибке ввода имени ")
    print("\nТест № EXP-019 Пройден")

def test_reg_page_name_long(browser_reg_page):
    input_field = browser_reg_page.find_elements(*RegPageLoc.LOCATOR_INPUT_FIELD)
    input_field[0].send_keys("абвгдеежзиклмнопрстцфхцчшщъыьэюя")
    input_field[1].send_keys(fake_lastname)
    input_field[3].send_keys(fake_email)
    input_field[4].send_keys(fake_password)
    input_field[5].send_keys(fake_password)
    browser_reg_page.find_element(*RegPageLoc.LOCATOR_BUTTON_REGISTRATION).click()
    error_message = browser_reg_page.find_elements(*RegPageLoc.LOCATOR_ERROR_MESS)
    name_error_message = error_message[0]

    assert name_error_message.text == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'

    print("\n Появилось сообщение об ошибке ввода имени ")
    print("\nТест № EXP-019 Пройден")

def test_reg_page_invalid_lastname(browser_reg_page):
    input_field = browser_reg_page.find_elements(*RegPageLoc.LOCATOR_INPUT_FIELD)
    input_field[0].send_keys(fake_firstname)
    input_field[1].send_keys(fake_lastname_en)
    input_field[3].send_keys(fake_email)
    input_field[4].send_keys(fake_password)
    input_field[5].send_keys(fake_password)
    browser_reg_page.find_element(*RegPageLoc.LOCATOR_BUTTON_REGISTRATION).click()
    error_message = browser_reg_page.find_elements(*RegPageLoc.LOCATOR_ERROR_MESS)
    last_name_error_message = error_message[0]

    assert last_name_error_message.text == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'
    print ("\n last_name_error_message.text")
    print("\n Появилось сообщение об ошибке ввода фамилии ")
    print("\nТест № EXP-020 Пройден")

def test_reg_page_invalid_lastname_short(browser_reg_page):
    input_field = browser_reg_page.find_elements(*RegPageLoc.LOCATOR_INPUT_FIELD)
    input_field[0].send_keys(fake_firstname)
    input_field[1].send_keys('д')
    input_field[3].send_keys(fake_email)
    input_field[4].send_keys(fake_password)
    input_field[5].send_keys(fake_password)
    browser_reg_page.find_element(*RegPageLoc.LOCATOR_BUTTON_REGISTRATION).click()
    error_message = browser_reg_page.find_elements(*RegPageLoc.LOCATOR_ERROR_MESS)
    last_name_error_message = error_message[0]

    assert last_name_error_message.text == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'

    print("\n Появилось сообщение об ошибке ввода фамилии ")
    print("\nТест № EXP-020 Пройден")

def test_reg_page_invalid_lastname_long(browser_reg_page):
    input_field = browser_reg_page.find_elements(*RegPageLoc.LOCATOR_INPUT_FIELD)
    input_field[0].send_keys(fake_firstname)
    input_field[1].send_keys('абвгдеежзиклмнопрстцфхцчшщъыьэюя')
    input_field[3].send_keys(fake_email)
    input_field[4].send_keys(fake_password)
    input_field[5].send_keys(fake_password)
    browser_reg_page.find_element(*RegPageLoc.LOCATOR_BUTTON_REGISTRATION).click()
    error_message = browser_reg_page.find_elements(*RegPageLoc.LOCATOR_ERROR_MESS)
    lastname_error_message = error_message[0]

    assert lastname_error_message.text == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'

    print("\n Появилось сообщение об ошибке ввода фамилии ")
    print("\nТест № EXP-020 Пройден")

def test_reg_page_invalid_mail(browser_reg_page):
    input_field = browser_reg_page.find_elements(*RegPageLoc.LOCATOR_INPUT_FIELD)
    input_field[0].send_keys(fake_firstname)
    input_field[1].send_keys(fake_lastname)
    input_field[3].send_keys('fjtuju')
    input_field[4].send_keys(fake_password)
    input_field[5].send_keys(fake_password)
    browser_reg_page.find_element(*RegPageLoc.LOCATOR_BUTTON_REGISTRATION).click()
    error_message = browser_reg_page.find_elements(*RegPageLoc.LOCATOR_ERROR_MESS)
    mail_error_message = error_message[0]

    assert  mail_error_message.text == 'Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru'

    print("\n Появилось сообщение об ошибке ввода адреса электронной почты или номера мобильного телефона ")
    print("\nТест № EXP-021 Пройден")


def test_reg_page_invalid_password(browser_reg_page):
    input_field = browser_reg_page.find_elements(*RegPageLoc.LOCATOR_INPUT_FIELD)
    input_field[0].send_keys(fake_firstname)
    input_field[1].send_keys(fake_lastname)
    input_field[3].send_keys(fake_email)
    input_field[4].send_keys('12345')
    input_field[5].send_keys(fake_password)
    browser_reg_page.find_element(*RegPageLoc.LOCATOR_BUTTON_REGISTRATION).click()
    error_message = browser_reg_page.find_elements(*RegPageLoc.LOCATOR_ERROR_MESS)
    password_error_message = error_message[0]

    assert password_error_message.text == 'Длина пароля должна быть не менее 8 символов'

    print("\n Появилось сообщение об ошибке в выборе пароля ")
    print("\nТест № EXP-021 Пройден")

def test_reg_page_invalid_password(browser_reg_page):
    input_field = browser_reg_page.find_elements(*RegPageLoc.LOCATOR_INPUT_FIELD)
    input_field[0].send_keys(fake_firstname)
    input_field[1].send_keys(fake_lastname)
    input_field[3].send_keys(fake_email)
    input_field[4].send_keys('12345678')
    input_field[5].send_keys(fake_password)
    browser_reg_page.find_element(*RegPageLoc.LOCATOR_BUTTON_REGISTRATION).click()
    error_message = browser_reg_page.find_elements(*RegPageLoc.LOCATOR_ERROR_MESS)
    password_error_message = error_message[0]

    assert password_error_message.text == 'Пароль должен содержать хотя бы одну заглавную букву'

    print("\n Появилось сообщение об ошибке в выборе пароля ")
    print("\nТест № EXP-022 Пройден")

def test_reg_page_invalid_password(browser_reg_page):
    input_field = browser_reg_page.find_elements(*RegPageLoc.LOCATOR_INPUT_FIELD)
    input_field[0].send_keys(fake_firstname)
    input_field[1].send_keys(fake_lastname)
    input_field[3].send_keys(fake_email)
    input_field[4].send_keys('12345678Д')
    input_field[5].send_keys(fake_password)
    browser_reg_page.find_element(*RegPageLoc.LOCATOR_BUTTON_REGISTRATION).click()
    error_message = browser_reg_page.find_elements(*RegPageLoc.LOCATOR_ERROR_MESS)
    password_error_message = error_message[0]

    assert password_error_message.text == 'Пароль должен содержать только латинские буквы'

    print("\n Появилось сообщение об ошибке в выборе пароля ")
    print("\nТест № EXP-022 Пройден")

def test_reg_page_invalid_password(browser_reg_page):
    input_field = browser_reg_page.find_elements(*RegPageLoc.LOCATOR_INPUT_FIELD)
    input_field[0].send_keys(fake_firstname)
    input_field[1].send_keys(fake_lastname)
    input_field[3].send_keys(fake_email)
    input_field[4].send_keys('12345678S')
    input_field[5].send_keys(fake_password)
    browser_reg_page.find_element(*RegPageLoc.LOCATOR_BUTTON_REGISTRATION).click()
    error_message = browser_reg_page.find_elements(*RegPageLoc.LOCATOR_ERROR_MESS)
    password_error_message = error_message[0]

    assert password_error_message.text == 'Пароль должен содержать хотя бы одну строчную букву'

    print("\n Появилось сообщение об ошибке в выборе пароля ")
    print("\nТест № EXP-022 Пройден")

def test_reg_page_invalid_password(browser_reg_page):
    input_field = browser_reg_page.find_elements(*RegPageLoc.LOCATOR_INPUT_FIELD)
    input_field[0].send_keys(fake_firstname)
    input_field[1].send_keys(fake_lastname)
    input_field[3].send_keys(fake_email)
    input_field[4].send_keys('12345678s')
    input_field[5].send_keys(fake_password)
    browser_reg_page.find_element(*RegPageLoc.LOCATOR_BUTTON_REGISTRATION).click()
    error_message = browser_reg_page.find_elements(*RegPageLoc.LOCATOR_ERROR_MESS)
    password_error_message = error_message[0]

    assert password_error_message.text == 'Пароль должен содержать хотя бы одну заглавную букву'

    print("\n Появилось сообщение об ошибке в выборе пароля ")
    print("\nТест № EXP-022 Пройден")

def test_reg_page_invalid_password(browser_reg_page):
    input_field = browser_reg_page.find_elements(*RegPageLoc.LOCATOR_INPUT_FIELD)
    input_field[0].send_keys(fake_firstname)
    input_field[1].send_keys(fake_lastname)
    input_field[3].send_keys(fake_email)
    input_field[4].send_keys(fake_password)
    input_field[5].send_keys('12345678Ss')
    browser_reg_page.find_element(*RegPageLoc.LOCATOR_BUTTON_REGISTRATION).click()
    error_message = browser_reg_page.find_elements(*RegPageLoc.LOCATOR_ERROR_MESS)
    password_error_message = error_message[0]

    assert password_error_message.text == 'Пароли не совпадают'

    print("\n Появилось сообщение об ошибке подтверждения пароля ")
    print("\nТест № EXP-023 Пройден")