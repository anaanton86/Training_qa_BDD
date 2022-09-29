from browser import Browser
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from unittest import TestCase


class BasePage(Browser, TestCase):
    def wait_for_elem(self, by, selector):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((by, selector)))

    def verify_page_title(self, expected):
        actual = self.driver.title
        assert actual == expected, "page title not ok"

    def verify_page_url(self, expected):
        actual = self.driver.current_url
        assert actual == expected, "page url not ok"

    # def press_enter(self, elem):
    #     elem.send_keys(Keys.ENTER)




