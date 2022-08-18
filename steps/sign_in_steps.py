from behave import *

'''
given, when, then, and, but - sintaxa gherkin
given - seteaza situatia initiala
when - pasii din test
then - validari din test
'''

''' 
exemplu:
Given I'm a user on sign in page
When I click forgot pass
When I input correct email
And I click reset pass
Then I see success msg and get email
'''

@given('Sign in: I navigate to sign in page')
def step_impl(context):
    context.sign_in_page.navigate_to_sign_in_page()

@when('Sign in: I click on forgot password')
def step_impl(context):
    context.sign_in_page.click_forgot_pass_link()

@when('Sign in: I login using user/pass combo')
def step_impl(context):
    context.sign_in_page.set_email()
    context.sign_in_page.set_password()
    context.sign_in_page.click_login_button()

