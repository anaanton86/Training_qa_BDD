from behave import *

@when('Sign up: I select personal option')
def step_impl(context):
    context.sign_up_page.click_personal_radio_button()
    context.sign_up_page.click_continue_button()

@when('Sign up: I complete first and last name inputs')
def step_impl(context):
    context.sign_up_page.complete_input('Ana')
    context.sign_up_page.click_continue_button_firstname()
    context.sign_up_page.complete_input('Anton')
    context.sign_up_page.click_continue_button_lastname()

@when('Sign up: I complete email input "{email}"')
def step_impl(context, email):
    context.sign_up_page.complete_input(email)
    context.sign_up_page.press_enter()

@then('Sign up: I validate error message is as expected "{message}"')
def step_impl(context, message):
    context.sign_up_page.validate_email_error(message)

