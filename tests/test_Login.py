from pageObjects.LoginPage import Login
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from selenium.common.exceptions import TimeoutException, WebDriverException
import logging
import time  # Import time for timestamping screenshots

class Test_001_Login:
    baseUrl = "http://automationexercise.com"
    signup_name = "Marial"
    email_name = "mariallugare@gmail.com"
    password = "Doralove91!"  # Consider secure storage

    def test_homePageTitle(self, setup):
        driver = setup
        driver.get(self.baseUrl)
        try:
            assert driver.title == "Automation Exercise"
        except AssertionError:
            screenshot_name = f".\\Screenshot\\test_homePageTitle_{int(time.time())}.png"  # Use timestamp for unique names
            driver.save_screenshot(screenshot_name)
            assert False
        finally:
            driver.close()

    def test_login(self, setup):
        driver = setup
        driver.get(self.baseUrl)
        lp = Login(driver)

        try:
            wait = WebDriverWait(driver, 20)

            # Wait for elements and perform login actions
            # ... (your existing code)

            # Assertions for successful login
            # ... (your existing code)

        except (TimeoutException, WebDriverException) as e:
            screenshot_name = f".\\Screenshot\\test_login_{int(time.time())}.png"  # Use timestamp for unique names
            driver.save_screenshot(screenshot_name)
            logging.error(f"Error during login: {e}")
            raise