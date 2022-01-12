from .base_page import BasePage
from selenium.webdriver.common.by import By


class LandingPage(BasePage):
    PAGE_ELEMENT_LOCATOR = (By.XPATH, "//h1[contains(text(),'A co-parenting app solution')]")

    def click_signup(self):
        self.driver.find_element_by_link_text('Sign up').click()

    def click_login(self):
        self.driver.find_element_by_link_text('Log in').click()
    