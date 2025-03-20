import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, expected_conditions


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://qa-scooter.praktikum-services.ru/"

    def find_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

    def click_element(self, locator):
        self.find_element(locator).click()

    def input_text(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def wait_for_new_tab(self, driver, original_window, timeout=60):
        WebDriverWait(driver, timeout).until(EC.number_of_windows_to_be(2))
        return [window for window in driver.window_handles if window != original_window][0]

    def close_new_tab_and_switch_back(self, driver, original_window):
        if len(driver.window_handles) > 1:
            driver.close()
            driver.switch_to.window(original_window)

    def wait_for_url_in_new_tab(self, driver, url_part, timeout=60):
        WebDriverWait(driver, timeout).until(lambda d: url_part in d.current_url)
        current_url = driver.current_url
        allure.attach(current_url, name="New Tab URL", attachment_type=allure.attachment_type.TEXT)
        return current_url
