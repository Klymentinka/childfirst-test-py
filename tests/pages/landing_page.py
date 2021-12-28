from .base_page import BasePage
import settings

class LandingPage(BasePage):
    
    XPATH_VERIFY ="//h1[contains(text(),'A co-parenting app solution')]"
    
    def load(self):
        self.driver.get(settings.LANDING_URL)
        

    def click_signup(self):
        self.driver.find_element_by_link_text('Sign up').click()
    