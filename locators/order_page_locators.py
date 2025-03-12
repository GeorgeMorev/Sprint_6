from selenium.webdriver.common.by import By

class OrderPageLocators:
    NAME = (By.XPATH, "//input[@placeholder='* Имя']")
    LAST_NAME = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_STATION = (By.CLASS_NAME, 'select-search__input')
    PHONE = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")
    MISS = (By.XPATH, "/html/body/div/div/div[2]/div[3]")
    DATE = (By.CSS_SELECTOR, "input[placeholder='* Когда привезти самокат']")
    RENTAL_PERIOD = (By.XPATH, "//div[contains(text(), 'Срок аренды')]/parent::div")
    RENTAL_PERIOD_OPTION = (By.XPATH, "//div[@class='Dropdown-option' and text()='{}']")
    COLOR_CHECKBOX = (By.ID, "{}")
    COMMENT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    ORDER_BUTTON = (By.XPATH, "/html/body/div/div/div[2]/div[3]/button[2]")
    CONFIRM_BUTTON = (By.XPATH, "/html/body/div/div/div[2]/div[5]/div[2]/button[2]")
    SUCCESS_MESSAGE = (By.XPATH, "//div[contains(@class, 'Order_ModalHeader') and contains(., 'Заказ оформлен')]")