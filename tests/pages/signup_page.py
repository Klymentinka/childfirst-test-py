from .base_page import BasePage


class SignupPage(BasePage):
    XPATH_VERIFY = "//h1[contains(text(),'Sign up Kids First')]"