from .base_page import BasePage


class SignupPage(BasePage):
        
    def verify(self):
        self.driver.find_element_by_xpath("//h1[contains(text(),'Sign up Kids First')]")
