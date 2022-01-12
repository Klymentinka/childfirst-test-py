from .base_page import BasePage
from selenium.webdriver.common.by import By

class SignupPage(BasePage):
    PAGE_ELEMENT_LOCATOR = (By.XPATH,"//h1[contains(text(),'Sign up Kids First')]")