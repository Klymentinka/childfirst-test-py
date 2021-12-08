from selenium import webdriver
from basetest import TestBase
from webdriver_manager.chrome import ChromeDriverManager

from tests.pages.landing_page import LandingPage

class TestLanding(TestBase):
    def test_open(self):
        landing_page = LandingPage(self.driver)
        landing_page.verify()
    
