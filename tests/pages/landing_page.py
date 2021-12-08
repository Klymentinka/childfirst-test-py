from selenium.webdriver import Remote as WebDriver

class LandingPage():
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.driver.get("http://localhost:3000/#")
    
    def verify(self):
        self.driver.find_element_by_xpath("//h1[contains(text(),'A co-parenting app solution')]")
    