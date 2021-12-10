from selenium.webdriver import Remote as WebDriver
from tests.pages.signup_page import SignupPage
from .base_page import BasePage


class LandingPage(BasePage):
    
    XPATH_VERIFY ="//h1[contains(text(),'A co-parenting app solution')]"
    
    def __init__(self, driver: WebDriver, url):
        super().__init__(driver)
        self.driver.get(url)
    
    def click_signup(self):
        self.driver.find_element_by_link_text('Sign up').click()
        return SignupPage(self.driver)
    