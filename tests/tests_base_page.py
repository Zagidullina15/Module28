from locators import *
from settings import fake_login, fake_phone, fake_email, invalid_ls


def test_tab_switching(browser):
    browser.find_element( *AutoPageLoc.LOCATOR_MAIL_TAB ).click()
    assert browser.find_element( *AutoPageLoc.LOCATOR_MAIL_FIELD ).text == 'Электронная почта'
    print( "\nвкладка 'Почта' активна" )

    browser.find_element( *AutoPageLoc.LOCATOR_PHONE_TAB ).click()
    assert browser.find_element( *AutoPageLoc.LOCATOR_PHONE_FIELD ).text == 'Мобильный телефон'
    print( "\nвкладка 'Tелефон' активна" )

    browser.find_element( *AutoPageLoc.LOCATOR_LOGIN_TAB ).click()
    assert browser.find_element( *AutoPageLoc.LOCATOR_LOGIN_FIELD ).text == 'Логин'
    print( "\nвкладка 'Логин' активна" )

    browser.find_element( *AutoPageLoc.LOCATOR_LS_TAB ).click()
    assert browser.find_element( *AutoPageLoc.LOCATOR_LS_FIELD ).text == 'Лицевой счёт'
    print( "\nвкладка 'Лицевой счёт' активна" )

    print( "\nТест № EXP-003 Пройден" )


def test_tab_auto_switching_phone(browser):
    browser.find_element( *AutoPageLoc.LOCATOR_MAIL_TAB ).click()
    browser.find_element( *AutoPageLoc.LOCATOR_MAIL_FIELD_ACTIV ).send_keys( fake_phone )
    browser.find_element( *AutoPageLoc.LOCATOR_PASSWORD_TAB ).click()

    assert browser.find_element( *AutoPageLoc.LOCATOR_PHONE_FIELD ).text == 'Мобильный телефон'
    print( "\nПереход на таб 'Телефон' с таб 'Почта' произошел " )
    print( "\nТест № EXP-004 Пройден" )


def test_tab_auto_switching_mail(browser):
    browser.find_element( *AutoPageLoc.LOCATOR_PHONE_FIELD_ACTIV ).send_keys( fake_email )
    browser.find_element( *AutoPageLoc.LOCATOR_PASSWORD_TAB ).click()
    assert browser.find_element( *AutoPageLoc.LOCATOR_MAIL_FIELD ).text == 'Электронная почта'
    print( "\nПереход на таб 'Почта'с таб 'Телефон' произошел " )

    browser.find_element( *AutoPageLoc.LOCATOR_LS_TAB ).click()
    browser.find_element( *AutoPageLoc.LOCATOR_LS_FIELD_ACTIV ).send_keys( fake_email )
    browser.find_element( *AutoPageLoc.LOCATOR_PASSWORD_TAB ).click()
    assert browser.find_element( *AutoPageLoc.LOCATOR_MAIL_FIELD ).text == 'Электронная почта'
    print( "\nПереход на таб 'Почта' с таб 'Лицевой счет' произошел " )

    browser.find_element( *AutoPageLoc.LOCATOR_LOGIN_TAB ).click()
    browser.find_element( *AutoPageLoc.LOCATOR_LOGIN_FIELD_ACTIV ).send_keys( fake_email )
    browser.find_element( *AutoPageLoc.LOCATOR_PASSWORD_TAB ).click()
    assert browser.find_element( *AutoPageLoc.LOCATOR_MAIL_FIELD ).text == 'Электронная почта'
    print( "\nПереход на таб 'Почта' с таб 'Логин' произошел " )

    print( "\nТест № EXP-005 Пройден" )


def test_tab_auto_switching_login(browser):
    browser.find_element( *AutoPageLoc.LOCATOR_PHONE_FIELD_ACTIV ).send_keys( fake_login )
    browser.find_element( *AutoPageLoc.LOCATOR_PASSWORD_TAB ).click()
    assert browser.find_element( *AutoPageLoc.LOCATOR_LOGIN_FIELD ).text == 'Логин'
    print( "\nПереход на таб 'Логин'с таб 'Телефон' произошел " )

    browser.find_element( *AutoPageLoc.LOCATOR_MAIL_TAB ).click()
    browser.find_element( *AutoPageLoc.LOCATOR_MAIL_FIELD_ACTIV ).send_keys( fake_login )
    browser.find_element( *AutoPageLoc.LOCATOR_PASSWORD_TAB ).click()
    assert browser.find_element( *AutoPageLoc.LOCATOR_LOGIN_FIELD ).text == 'Логин'
    print( "\nПереход на таб 'Логин'с таб 'Почта' произошел " )

    browser.find_element( *AutoPageLoc.LOCATOR_LS_TAB ).click()
    browser.find_element( *AutoPageLoc.LOCATOR_LS_FIELD_ACTIV ).send_keys( fake_login )
    browser.find_element( *AutoPageLoc.LOCATOR_PASSWORD_TAB ).click()
    assert browser.find_element( *AutoPageLoc.LOCATOR_LOGIN_FIELD ).text == 'Логин'
    print( "\nПереход на таб 'Логин'с таб 'Лицевой счет' произошел " )

    print( "\nТест № EXP-006 Пройден" )


def test_tab_auto_switching_ls(browser):
    browser.find_element( *AutoPageLoc.LOCATOR_MAIL_TAB ).click()
    browser.find_element( *AutoPageLoc.LOCATOR_MAIL_FIELD_ACTIV ).send_keys( invalid_ls )
    browser.find_element( *AutoPageLoc.LOCATOR_PASSWORD_TAB ).click()
    assert browser.find_element( *AutoPageLoc.LOCATOR_LS_FIELD ).text == 'Лицевой счёт'
    print( "\nПереход на таб 'Лицевой счет'с таб 'Почта' произошел " )
    print( "\nТест № EXP-007 Пройден" )