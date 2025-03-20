import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from .base_page import BasePage
from locators.order_page_locators import OrderPageLocators
from selenium.webdriver.common.by import By


class OrderPage(BasePage):
    @allure.step("Заполнение раздела 'Про аренду")
    def fill_rent_info(self, date: str, period: str, color: str, comment: str):
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

    @allure.step("Заполнение персональных данных")
    def fill_personal_info(self, name: str, last_name: str, address: str, metro: str, phone: str):
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

    @allure.step("Выбор периода аренды с улучшенным ожиданием")
    def _select_rental_period(self, period: str):
        try:
            WebDriverWait(self.driver, 15).until(
                EC.element_to_be_clickable(OrderPageLocators.RENTAL_PERIOD)
            ).click()
            WebDriverWait(self.driver, 15).until(
                EC.visibility_of_element_located(
                    OrderPageLocators.DROPDOWN_MENU
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

    @allure.step("Выбор цвета самоката")
    def _select_color(self, color: str):
        color_locator = (By.CSS_SELECTOR, f"input[id='{color}']")
        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable(color_locator)
        ).click()

    @allure.step("Подтверждение заказа")
    def confirm_order(self):
        try:
            confirm_button = WebDriverWait(self.driver, 15).until(
                EC.element_to_be_clickable(OrderPageLocators.CONFIRM_BUTTON)
            )
            confirm_button.click()
        except Exception as e:
            self.driver.save_screenshot("confirm_error.png")
            raise e

    @allure.step("Получение текста успешного оформления заказа")
    def get_success_message(self) -> str:
        return WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located(OrderPageLocators.SUCCESS_MESSAGE)
        ).text
