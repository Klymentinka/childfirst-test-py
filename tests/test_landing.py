from pytest_bdd import scenarios, given, when, then
from tests.pages.landing_page import LandingPage
from tests.pages.signup_page import SignupPage

scenarios('./features/landing.feature')

@given('we are on landing page')
def step_impl(browser):
    landing_page = LandingPage(browser)
    landing_page.load()

@when('we click on singup button')
def step_impl(browser):
    landing_page = LandingPage(browser)
    landing_page.click_signup()

@then('we are on singup page')
def step_impl(browser):
    signup_page = SignupPage(browser)
    signup_page.verify()
