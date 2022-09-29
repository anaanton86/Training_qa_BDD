from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
from time import sleep


class SignUpPage(BasePage):
    # locators
    LOGIN_BUTTON = (By.XPATH, '//button[@data-test-id="go-to-login-btn"]')
    BUSINESS_RADIO_BUTTON = (By.XPATH, '//input[@value="business"]') # sau find label??
    PERSONAL_RADIO_BUTTON = (By.XPATH, '//input[@value="personal"]')
    CONTINUE_BUTTON = (By.XPATH, '//button[@data-test-id="select-account-continue-btn"]')
    # CONTINUE_BUTTON = (By.XPATH, '//span[text()="CONTINUE"]/parent::button')  # locator general
    FIRST_NAME_LABEL = (By.XPATH, '//strong[text()="last name..."]')
    INPUT = (By.XPATH, '//input')
    CONTINUE_BUTTON_FIRSTNAME = (By.XPATH, '//button[@data-test-id="first-name-continue-btn"]')
    LAST_NAME_INPUT = (By.XPATH, '//strong[text()="last name..."]//parent::span/parent::div/parent::div//input')
    CONTINUE_BUTTON_LASTNAME = (By.XPATH, '//button[@data-test-id="last-name-continue-btn"]')
    EMAIL_INPUT = (By.XPATH, '')
    EMAIL_ERROR = (By.XPATH, '//p[contains(text(), "address")]')
    CONTINUE_BUTTON_EMAIL = (By.XPATH, '//button[@data-test-id="email-continue-btn"]')
    PASSWORD_INPUT = (By.XPATH, '')
    CONTINUE_BUTTON_PASS = (By.XPATH, '//button[@data-test-id="password-continue-btn"]')
    CONFIRM_PASSWORD_INPUT = (By.XPATH, '')
    SIGN_UP_BUTTON = (By.XPATH, '//button[@data-test-id="sign-up-btn"]')
    # PRESS_ENTER = (By.XPATH, '//strong[text()="ENTER"]') # not ok

    # exemplu pt radio button list
    # EDUCATION_LIST = (By.XPATH, '//input[@type="radio"]')


    def click_login_button(self):
        self.wait_for_elem(*self.LOGIN_BUTTON)
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    def click_business_radio_button(self):
        self.wait_for_elem(*self.BUSINESS_RADIO_BUTTON)
        self.driver.find_element(*self.BUSINESS_RADIO_BUTTON).click()

    def click_personal_radio_button(self):
        self.wait_for_elem(*self.PERSONAL_RADIO_BUTTON)
        self.driver.find_element(*self.PERSONAL_RADIO_BUTTON).click()

    def click_continue_button(self):
        self.wait_for_elem(*self.CONTINUE_BUTTON)
        sleep(1)
        self.driver.find_element(*self.CONTINUE_BUTTON).click()

    def press_enter(self):
        self.wait_for_elem(*self.INPUT)
        sleep(1)
        self.driver.find_element(*self.INPUT).send_keys(Keys.ENTER)

    def complete_input(self, value):
        self.wait_for_elem(*self.INPUT)
        sleep(1)
        self.driver.find_element(*self.INPUT).send_keys(value)

    # steps
    def validate_first_name_label_is_displayed(self):
        assert self.driver.find_element(*self.FIRST_NAME_LABEL).is_displayed(), "first name label not displayed"

    def complete_first_name_input(self, first_name):
        # make sure we are on the right step in the wizard
        self.validate_first_name_label_is_displayed()
        # complete first name input
        self.driver.find_element(*self.INPUT).send_keys(first_name)

    def complete_last_name_input(self, last_name):
        self.wait_for_elem(*self.LAST_NAME_INPUT)
        self.driver.find_element(*self.LAST_NAME_INPUT).send_keys(last_name)

    def click_continue_button_firstname(self):
        self.wait_for_elem(*self.CONTINUE_BUTTON_FIRSTNAME)
        self.driver.find_element(*self.CONTINUE_BUTTON_FIRSTNAME).click()

    def click_continue_button_lastname(self):
        self.wait_for_elem(*self.CONTINUE_BUTTON_LASTNAME)
        self.driver.find_element(*self.CONTINUE_BUTTON_LASTNAME).click()

    def click_continue_button_email(self):
        self.wait_for_elem(*self.CONTINUE_BUTTON_EMAIL)
        self.driver.find_element(*self.CONTINUE_BUTTON_EMAIL).click()

    # exemplu pt radio button list
    # def toggle_education_radio_button(self, index):
    #     self.driver.find_elements(*self.EDUCATION_LIST)[index].click()


    def validate_email_error(self, error_text):
        actual = self.driver.find_element(*self.EMAIL_ERROR).text
        assert self.driver.find_element(*self.EMAIL_ERROR).is_displayed(), 'error not displayed'
        assert actual == error_text, f'Expected {error_text}, but found {actual}'




