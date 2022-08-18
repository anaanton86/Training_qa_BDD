from behave import *

@when('Forgot pass: I write my email "{email}"')
def set_impl(context, email):
    context.forgot_password_page.set_email(email)

@then('Forgot pass: I validate that send email button is disabled')
def set_impl(context):
    context.forgot_password_page.validate_send_email_button_is_disabled()

@then('Forgot pass: I validate invalid email error is displayed')
def set_impl(context):
    context.forgot_password_page.validate_invalid_email_error()

@then('Forgot pass: I validate that send email button is enabled')
def set_impl(context):
    context.forgot_password_page.validate_send_email_button_is_enabled()


