from selenium.webdriver import Remote as WebDriver


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver