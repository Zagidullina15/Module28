from selenium.webdriver.common.by import By
"""Локаторы для странице авторизации"""
class AutoPageLoc:
    LOCATOR_PHONE_TAB=(By.ID, 't-btn-tab-phone')
    LOCATOR_PHONE_FIELD = (By.XPATH, '//span[contains(text(),"Мобильный телефон")]')
    LOCATOR_PHONE_FIELD_ACTIV = (By.ID, 'username')
    LOCATOR_MAIL_TAB =(By.ID,  't-btn-tab-mail')
    LOCATOR_MAIL_FIELD = (By.XPATH, '//span[contains(text(),"Электронная почта")]')
    LOCATOR_MAIL_FIELD_ACTIV = (By.ID, 'username')
    LOCATOR_LOGIN_TAB = (By.ID, 't-btn-tab-login')
    LOCATOR_LOGIN_FIELD = (By.XPATH, '//span[contains(text(),"Логин")]')
    LOCATOR_LOGIN_FIELD_ACTIV = (By.ID, 'username')
    LOCATOR_LS_TAB = (By.ID, 't-btn-tab-ls')
    LOCATOR_LS_FIELD = (By.XPATH, '//span[contains(text(),"Лицевой счёт")]')
    LOCATOR_LS_FIELD_ACTIV = (By.ID, 'username')
    LOCATOR_PASSWORD_TAB = (By.ID, 'password')
    LOCATOR_ENTER_TAB = (By.ID, 'kc-login')
    LOCATOR_LK_TAB = (By.ID, 'lk-btn') # локатор для личного кабинета
    LOCATOR_ERROR = (By.ID, 'form-error-message')
    LOCATOR_FORGOT_PASSWORD = (By.ID, 'forgot_password')
    LOCATOR_ERROR_MESS = (By.XPATH, '//span[contains(@class, "rt-input-container__meta")]')
    LOCATOR_REG_TAB = (By.ID, 'kc-register')
    """Локаторы для соц.сетей"""
    LOCATOR_VK_TAB = (By.ID, 'oidc_vk')
    LOCATOR_VK_FIELD = (By.XPATH, '//b[text()="ВКонтакте"]')
    LOCATOR_OK_TAB = (By.ID, 'oidc_ok')
    LOCATOR_OK_FIELD = (By.CLASS_NAME, 'ext-widget_h_tx')
    LOCATOR_MAILRU_TAB = (By.ID, 'oidc_mail')
    LOCATOR_MAILRU_FIELD = (By.CLASS_NAME, 'header__logo')
    LOCATOR_GOOGLE_TAB = (By.ID, 'oidc_google')
    LOCATOR_GOOGLE_FIELD = (By.CLASS_NAME, 'kHn9Lb')
    LOCATOR_YANDEX_TAB = (By.ID, 'card-container__title')
    LOCATOR_YANDEX_FIELD = (By.CSS_SELECTOR,'.passp-add-account-page-title')
    """Локаторы для страницы смены пароля"""
class PassRecLoc:
    LOCATOR_PassRec_FIELD = (By.CLASS_NAME, 'card-container__title')
    LOCATOR_PHONE_TAB = (By.ID, 't-btn-tab-phone')
    LOCATOR_PHONE_FIELD = (By.ID, 'username')
    LOCATOR_MAIL_TAB = (By.ID, 't-btn-tab-mail')
    LOCATOR_MAIL_FIELD = (By.ID, 'username')
    LOCATOR_LOGIN_TAB = (By.ID, 't-btn-tab-login')
    LOCATOR_LOGIN_FIELD = (By.ID, 'username')
    LOCATOR_LS_TAB = (By.ID, 't-btn-tab-ls')
    LOCATOR_LS_FIELD = (By.ID, 'username')
    LOCATOR_BUTTON_CONTINUE = ( By.ID, 'reset')
    LOCATOR_CODE_FIELD = (By.CLASS_NAME, 'card-container__title')
    """Локаторы для страницы регистрации"""
class RegPageLoc:
    LOCATOR_REG_FIELD = (By.CLASS_NAME, 'card-container__title')
    LOCATOR_BUTTON_REGISTRATION = (By.NAME, 'register')
    LOCATOR_REGISTRATION_CODE_FIELD = (By.CLASS_NAME, 'card-container__title')

    LOCATOR_ERROR_MESS = (By.XPATH, '//span[contains(@class, "rt-input-container__meta")]')
    LOCATOR_INPUT_FIELD = (By.XPATH, '//input[contains(@class, "rt-input__input")]')