from .base_page import BasePage
from selenium.webdriver.common.by import By

class SignupPage(BasePage):
    PAGE_ELEMENT_LOCATOR = (By.XPATH,"//h1[contains(text(),'Sign up Kids First')]")
    PAGE_PATH = '/Signup'

    def enter_login_pass_confpass(self, email, password, confirm_password):
       self.driver.find_element_by_name("email").send_keys(email)
       self.driver.find_element_by_name("password").send_keys(password)
       self.driver.find_element_by_name("password2").send_keys(confirm_password)

    def click_signup(self):
        self.driver.find_element_by_class_name("form-input-btn").click()
