from selenium.webdriver import Remote as WebDriver
import settings


class BasePage:
    
    PAGE_ELEMENT_LOCATOR = None
    PAGE_PATH = ''
    
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def load(self):
        self.driver.get(settings.LANDING_URL + self.PAGE_PATH)
    
    def verify(self):
        self.driver.find_element(*self.PAGE_ELEMENT_LOCATOR)
