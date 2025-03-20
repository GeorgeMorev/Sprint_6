import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from .base_page import BasePage
from locators.home_page_locators import HomePageLocators
from locators.base_page_locators import BasePageLocators


class HomePage(BasePage):
    @allure.step("Принять куки")
    def accept_cookies(self):
        self.click_element(BasePageLocators.COOKIE_BANNER)

    @allure.step("Кликнуть на вопрос по индексу")
    def click_question(self, index):
        questions = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(HomePageLocators.QUESTION)
        )

        # Прокручиваем элемент в видимую область
        self.driver.execute_script("arguments[0].scrollIntoView();", questions[index])

        # Ожидаем, что элемент кликабельный
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(questions[index])
        )

        questions[index].click()

    @allure.step("Получить текст ответа по индексу")
    def get_answer_text(self, index):
        answers = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(HomePageLocators.ANSWER)
        )
        return answers[index].text

    @allure.step("Кликнуть кнопку заказа в header или footer")
    def click_order_button(self, position='header'):
        locator = (HomePageLocators.ORDER_BUTTON_HEADER if position == 'header'
                   else HomePageLocators.ORDER_BUTTON_FOOTER)
        self.click_element(locator)

    @allure.step("Возвращает текущий URL страницы")
    def get_current_url(self):
        return self.driver.current_url

    @allure.step("Возвращает дескриптор текущего окна браузера")
    def get_current_window_handle(self):
        return self.driver.current_window_handle

    @allure.step("Переключиться на вкладку")
    def switch_to_window(self, window_handle):
        self.driver.switch_to.window(window_handle)

    @allure.step("Закрыть текущую вкладку и вернуться в исходное окно")
    def close_current_tab_and_switch_back(self, original_window):
        if len(self.driver.window_handles) > 1:
            self.driver.close()
            self.driver.switch_to.window(original_window)
            allure.attach(self.driver.current_url, name="Restored Window URL",
                          attachment_type=allure.attachment_type.TEXT)
