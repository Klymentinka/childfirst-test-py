from pytest_bdd import parsers, scenarios, given, when, then
from tests.pages.landing_page import LandingPage
from tests.pages.signin_page import SigninPage
from tests.pages.dashboard_page import DashboardPage

scenarios('./features/signin.feature')

# def pytest_bdd_before_step(browser):
#     print("Hello============================= " + browser)

@given('we are on signin page')
def signin_load(browser):
    signin_page = SigninPage(browser)
    signin_page.load()
    signin_page.verify()
    
@when(parsers.parse('we enter {email} and {password}'))
def signin_param(browser, email, password):
    signin_page = SigninPage(browser)
    signin_page.enter_login_password(email, password)

@when('click "Log in"')
def signin_param(browser, email, password):
    signin_page = SigninPage(browser)
    signin_page.click_login()

@then('we are on dashboard page')
def dashboard_verify(browser):
    dashboard_page = DashboardPage(browser)
    dashboard_page.verify()