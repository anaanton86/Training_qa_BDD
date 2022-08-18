from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class SignInPage(BasePage):
    EMAIL_INPUT = (By.XPATH, '//input[@placeholder="Enter your email"]')
    PASSWORD_INPUT = (By.XPATH, '//input[@placeholder="Enter your password"]')     #(//*[@focusable="false"])[1]
    LOGIN_BUTTON = (By.XPATH, '//button[@type="submit"]')
    FORGOT_PASS_LINK = (By.XPATH, '//a[text()="Forgot password?"]')
    SIGN_UP_LINK = (By.XPATH, '//a[@data-test-id="sign-up-link"]')

    def navigate_to_sign_in_page(self):
        self.driver.get('https://jules.app/sign-in')

    def set_email(self, email):
        self.wait_for_elem(*self.EMAIL_INPUT)
        self.driver.find_element(*self.EMAIL_INPUT).send_keys(email)

    def set_password(self, password):
        self.wait_for_elem(*self.PASSWORD_INPUT)
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)

    def click_login_button(self):
        self.wait_for_elem(*self.LOGIN_BUTTON)
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    def click_forgot_pass_link(self):
        self.wait_for_elem(*self.FORGOT_PASS_LINK)
        self.driver.find_element(*self.FORGOT_PASS_LINK).click()

    def click_sign_up_link(self):
        self.wait_for_elem(*self.SIGN_UP_LINK)
        self.driver.find_element(*self.SIGN_UP_LINK).click()






