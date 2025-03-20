import pytest
from selenium import webdriver
from pages.home_page import HomePage
from pages.order_page import OrderPage

@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.get("https://qa-scooter.praktikum-services.ru/")
    yield driver
    driver.quit()

@pytest.fixture
def home_page(driver):
    page = HomePage(driver)
    page.accept_cookies()
    return page

@pytest.fixture
def order_page(driver):
    return OrderPage(driver)