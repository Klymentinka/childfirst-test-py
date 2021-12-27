from behave import *

@given('we are on landing page')
def step_impl(context):
    pass

@when('we click on singup button')
def step_impl(context):
    assert True is not False

@then('we are on singup page')
def step_impl(context):
    assert context.failed is False