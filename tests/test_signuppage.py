from pytest_bdd import parsers, scenarios, given, when, then
from tests.pages.signup_page import SignupPage
from tests.pages.myinfo_page import MyinfoPage

scenarios('./features/signup.feature')

@given('we are on signup page')
def signup_load(browser):
    signup_page = SignupPage(browser)
    signup_page.load()
    signup_page.verify()
    
@when(parsers.parse('we enter {email} and {password} and {confirm_password}'))
def signup_param(browser, email, password, confirm_password):
    signup_page = SignupPage(browser)
    signup_page.enter_login_pass_confpass(email, password, confirm_password)

@when('click "Sign up"')
def signin_param(browser):
    signup_page = SignupPage(browser)
    signup_page.click_signup()

@then('we are on myinfo page')
def myinfo_verify(browser):
    myinfo_page = MyinfoPage(browser)
    myinfo_page.verify()