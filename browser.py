from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class Browser():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))   # fake chrome
    driver.implicitly_wait(10)
    driver.set_page_load_timeout(10)
    driver.maximize_window()
    driver.delete_all_cookies()

    def close(self):
        self.driver.close()



    