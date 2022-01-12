from .base_page import BasePage
from selenium.webdriver.common.by import By


class SigninPage(BasePage):
    PAGE_ELEMENT_LOCATOR = (By.XPATH, "//h1[contains(text(),'Log in Kids First')]")
    PAGE_PATH = '/Signin'

    def enter_login_password(self, email, password):
        self.driver.find_element_by_name("email").send_keys(email)
        self.driver.find_element_by_name("password").send_keys(password)

    def click_login(self):
        self.driver.find_element_by_class_name("form-input-btn").click()

