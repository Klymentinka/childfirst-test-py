from .base_page import BasePage
from selenium.webdriver.common.by import By

class MyinfoPage(BasePage):
    PAGE_ELEMENT_LOCATOR = (By.XPATH, '//button[text()="My Information"]')
    PAGE_PATH = '/MyInfo'