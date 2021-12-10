from selenium.webdriver import Remote as WebDriver


class BasePage:
    
    XPATH_VERIFY = ""
    
    def __init__(self, driver: WebDriver):
        self.driver = driver
    
    def verify(self):
        self.driver.find_element_by_xpath(self.XPATH_VERIFY)