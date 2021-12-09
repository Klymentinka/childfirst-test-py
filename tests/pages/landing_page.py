from selenium.webdriver import Remote as WebDriver
from tests.pages.signup_page import SignupPage


class LandingPage():
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.driver.get("http://localhost:3000/#")
    
    def verify(self):
        self.driver.find_element_by_xpath("//h1[contains(text(),'A co-parenting app solution')]")

    def click_signup(self):
        self.driver.find_element_by_xpath("//header/div[1]/div[2]/a[2]").click()
        return SignupPage(self.driver)
    