from selenium.webdriver import Remote as WebDriver


class SignupPage():
    def __init__(self, driver: WebDriver):
        self.driver = driver
        
    def verify(self):
        self.driver.find_element_by_xpath("//h1[contains(text(),'Sign up Kids First')]")
