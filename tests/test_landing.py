from basetest import TestBase
from tests.pages.landing_page import LandingPage

class TestLanding(TestBase):
    def test_open(self):
        landing_page = LandingPage(self.driver)
        landing_page.verify()
        signup_page = landing_page.click_signup()
        signup_page.verify()