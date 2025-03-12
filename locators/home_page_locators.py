from selenium.webdriver.common.by import By

class HomePageLocators:
    QUESTION = (By.XPATH, "//div[@data-accordion-component='AccordionItemButton']")
    ANSWER = (By.XPATH, "//div[@data-accordion-component='AccordionItemPanel']")
    ORDER_BUTTON_HEADER = (By.XPATH, "//button[@class='Button_Button__ra12g' and text()='Заказать']")
    ORDER_BUTTON_FOOTER = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Заказать']")