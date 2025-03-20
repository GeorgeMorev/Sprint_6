from selenium.webdriver.common.by import By


class BasePageLocators:
    SCOOTER_LOGO = (By.CLASS_NAME, 'Header_LogoScooter__3lsAR')
    YANDEX_LOGO = (By.CLASS_NAME, 'Header_LogoYandex__3TSOI')
    COOKIE_BANNER = (By.ID, 'rcc-confirm-button')
