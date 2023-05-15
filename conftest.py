import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

BASE_URL = 'https://b2c.passport.rt.ru'
#фикстура открытия и закрытия браузера
@pytest.fixture(scope = "session")
def browser():
    print('запуск браузера GoogleChrome')
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.maximize_window()
    browser.get(BASE_URL)
    yield browser

    print('конец сессии')
    browser.quit()

@pytest.fixture(scope = "session")
def browser_reg_page():

    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.maximize_window()
    browser.get(BASE_URL)
    browser.find_element(By.ID, 'kc-register').click()
    yield browser

    print('конец сессии')
    browser.quit()


@pytest.fixture(scope = "session")
def browser_PasRec_page():

    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.maximize_window()
    browser.get(BASE_URL)
    browser.find_element(By.ID, 'forgot_password').click()
    yield browser

    print('конец сессии')
    browser.quit()