import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.base_page_locators import BasePageLocators

@allure.feature('Тесты навигации через логотипы')
class TestLogoNavigation:
    @allure.title('Переход через логотип Самоката')
    @allure.description('Проверка редиректа на главную страницу через логотип Самоката')
    def test_scooter_logo_navigation(self, home_page, driver):
        with allure.step('Кликнуть на логотип Самоката'):
            home_page.click_element(BasePageLocators.SCOOTER_LOGO)
        
        with allure.step('Проверить URL после перехода'):
            current_url = driver.current_url
            allure.attach(current_url, name="Current URL", attachment_type=allure.attachment_type.TEXT)
            assert current_url == "https://qa-scooter.praktikum-services.ru/"

    @allure.title('Переход через логотип Яндекса')
    @allure.description('Проверка открытия новой вкладки с Дзеном через логотип Яндекса')
    def test_yandex_logo_navigation(self, home_page, driver):
        with allure.step('Запомнить текущее окно браузера'):
            original_window = driver.current_window_handle
        
        with allure.step('Кликнуть на логотип Яндекса'):
            home_page.click_element(BasePageLocators.YANDEX_LOGO)

        try:
            with allure.step('Дождаться открытия новой вкладки'):
                new_window = home_page.wait_for_new_tab(driver, original_window)

            with allure.step('Переключиться на новую вкладку'):
                driver.switch_to.window(new_window)

                with allure.step('Проверить URL в новой вкладке'):
                    current_url = home_page.wait_for_url_in_new_tab(driver, "dzen.ru")
                    assert "dzen.ru" in current_url or "yandex.ru" in current_url

        finally:
            with allure.step('Закрыть новую вкладку и вернуться в исходное окно'):
                if len(driver.window_handles) > 1:
                    driver.close()
                    driver.switch_to.window(original_window)
                    allure.attach(driver.current_url, name="Restored Window URL", attachment_type=allure.attachment_type.TEXT)