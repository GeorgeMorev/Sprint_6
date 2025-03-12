from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from .base_page import BasePage
from locators.order_page_locators import OrderPageLocators
from selenium.webdriver.common.by import By

class OrderPage(BasePage):
    def fill_rent_info(self, date: str, period: str, color: str, comment: str):
        """Заполнение раздела 'Про аренду'"""
        try:
            self.input_text(OrderPageLocators.DATE, date)
            self.driver.find_element(By.TAG_NAME, 'body').click()
            WebDriverWait(self.driver, 5).until(
                EC.invisibility_of_element_located((By.CLASS_NAME, "react-datepicker"))
            )
            self._select_rental_period(period)
            self._select_color(color)
            self.input_text(OrderPageLocators.COMMENT, comment)
            self.click_element(OrderPageLocators.ORDER_BUTTON)
            
        except Exception as e:
            self.driver.save_screenshot("rent_info_error.png")
            raise e

    def fill_personal_info(self, name: str, last_name: str, address: str, metro: str, phone: str):
        """Заполнение персональных данных"""
        try:
            self.input_text(OrderPageLocators.NAME, name)
            self.input_text(OrderPageLocators.LAST_NAME, last_name)
            self.input_text(OrderPageLocators.ADDRESS, address)
            self.click_element(OrderPageLocators.METRO_STATION)
            metro_locator = (By.XPATH, f"//div[text()='{metro}']")
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(metro_locator)
            ).click()
            self.input_text(OrderPageLocators.PHONE, phone)
            self.click_element(OrderPageLocators.NEXT_BUTTON)
            
        except Exception as e:
            self.driver.save_screenshot("personal_info_error.png")
            raise e

    def _select_rental_period(self, period: str):
        """Выбор периода аренды с улучшенным ожиданием"""
        try:
            WebDriverWait(self.driver, 15).until(
                EC.element_to_be_clickable(OrderPageLocators.RENTAL_PERIOD)
            ).click()
            WebDriverWait(self.driver, 15).until(
                EC.visibility_of_element_located(
                    (By.XPATH, "//div[@class='Dropdown-menu']")
                )
            )
            period_locator = (By.XPATH, f"//div[@class='Dropdown-option' and contains(., '{period}')]")
            option = WebDriverWait(self.driver, 15).until(
                EC.element_to_be_clickable(period_locator)
            )
            self.driver.execute_script("arguments[0].scrollIntoView(true);", option)
            option.click()
            
        except Exception as e:
            self.driver.save_screenshot("period_error.png")
            raise e

    def _select_color(self, color: str):
        """Выбор цвета самоката"""
        color_locator = (By.CSS_SELECTOR, f"input[id='{color}']")
        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable(color_locator)
        ).click()

    def confirm_order(self):
        """Подтверждение заказа"""
        try:
            confirm_button = WebDriverWait(self.driver, 15).until(
                EC.element_to_be_clickable(OrderPageLocators.CONFIRM_BUTTON)
            )
            confirm_button.click()
        except Exception as e:
            self.driver.save_screenshot("confirm_error.png")
            raise e
        
    def get_success_message(self) -> str:
        """Получение текста успешного оформления заказа"""
        return WebDriverWait(self.driver, 15).until(
        EC.visibility_of_element_located(OrderPageLocators.SUCCESS_MESSAGE)
    ).text