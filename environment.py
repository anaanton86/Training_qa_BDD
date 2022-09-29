from pages.sign_in_page import SignInPage
from pages.sign_up_page import SignUpPage
from pages.forgot_password_page import ForgotPasswordPage
from browser import Browser

def before_all(context):
    context.browser = Browser()
    context.sign_in_page = SignInPage()
    context.sign_up_page = SignUpPage()
    context.forgot_password_page = ForgotPasswordPage()

def after_all(context):
    context.browser.close()