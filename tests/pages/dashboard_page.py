from .base_page import BasePage
from selenium.webdriver.common.by import By


class DashboardPage(BasePage):
    PAGE_ELEMENT_LOCATOR = (By.LINK_TEXT, "My Dashboard")
    PAGE_PATH = '/dashboard'