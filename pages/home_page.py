from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from .base_page import BasePage
from locators.home_page_locators import HomePageLocators
from locators.base_page_locators import BasePageLocators


class HomePage(BasePage):
    def accept_cookies(self):
        """Принять куки"""
        self.click_element(BasePageLocators.COOKIE_BANNER)

    def click_question(self, index):
        """Кликнуть на вопрос по индексу"""
        questions = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(HomePageLocators.QUESTION)
        )
        questions[index].click()

    def get_answer_text(self, index):
        """Получить текст ответа по индексу"""
        answers = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(HomePageLocators.ANSWER)
        )
        return answers[index].text

    def click_order_button(self, position='header'):
        """Кликнуть кнопку заказа в header или footer"""
        locator = (HomePageLocators.ORDER_BUTTON_HEADER if position == 'header'
                   else HomePageLocators.ORDER_BUTTON_FOOTER)
        self.click_element(locator)