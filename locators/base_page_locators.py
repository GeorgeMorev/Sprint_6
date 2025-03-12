from selenium.webdriver.common.by import By

class BasePageLocators:
    SCOOTER_LOGO = (By.CLASS_NAME, 'Header_LogoScooter__3lsAR')
    YANDEX_LOGO = (By.XPATH, '/html/body/div/div/div/div[1]/div[1]/a[1]/img')
    COOKIE_BANNER = (By.ID, 'rcc-confirm-button')