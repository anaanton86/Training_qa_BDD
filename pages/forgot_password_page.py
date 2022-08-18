from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from time import sleep

class ForgotPasswordPage(BasePage):
    EMAIL_INPUT = (By.XPATH, '//input[@placeholder="Enter your email"]')
    SEND_EMAIL_BUTTON = (By.XPATH, '//button[@data-test-id="login-button"]')  # //*[text()="Send email"]/parent::button'
    BACK_TO_LOGIN_LINK = (By.XPATH, '//a[@data-test-id="sign-in-link"]')
    SIGN_UP_LINK = (By.XPATH, '//a[@data-test-id="sign-up-link"]')
    INVALID_EMAIL_ERROR = (By.XPATH, '//p[contains(text(), "email")]')
    INVALID_ERROR_LIST = (By.XPATH, '//p[contains(text(), "email")]')

    # def navigate_to_jules_pass(self):    # aici nu, utilizatorul incepe de pe sign in page = home page
    #     self.driver.get('https://jules.app/forgot-password')

    def set_email(self, email):
        self.wait_for_elem(*self.EMAIL_INPUT)
        self.driver.find_element(*self.EMAIL_INPUT).send_keys(email)

    def click_send_email_button(self):
        self.wait_for_elem(*self.SEND_EMAIL_BUTTON)
        self.driver.find_element(*self.SEND_EMAIL_BUTTON).click()

    def back_to_login_link(self):
        self.wait_for_elem(*self.BACK_TO_LOGIN_LINK)
        self.driver.find_element(*self.BACK_TO_LOGIN_LINK).click()

    def click_sign_up_link(self):
        self.wait_for_elem(*self.SIGN_UP_LINK)
        self.driver.find_element(*self.SIGN_UP_LINK).click()

    def validate_send_email_button_is_enabled(self):
        assert self.driver.find_element(*self.SEND_EMAIL_BUTTON).is_enabled(), "button is disabled"

    def validate_send_email_button_is_disabled(self):
        sleep(5)
        assert self.driver.find_element(*self.SEND_EMAIL_BUTTON).is_enabled() is not True, "button is enabled"

    def validate_invalid_email_error(self):
        assert self.driver.find_element(*self.INVALID_EMAIL_ERROR).is_displayed(), "error not displayed"
        assert self.driver.find_element(*self.INVALID_EMAIL_ERROR).text == 'Please enter a valid email address!', "wrong error"

    def validate_invalid_email_error_not_displayed(self):
        assert len(self.driver.find_elements (*self.INVALID_ERROR_LIST)) == 0, "error is displayed"