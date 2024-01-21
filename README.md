steps on how to run this project.

Step 1: Install Required Packages
Open a terminal or command prompt and run the following command to install the required packages:

bash
Copy code
pip install selenium pytest

Step 2: Download ChromeDriver
Download the ChromeDriver executable from the ChromeDriver Downloads page. Ensure that you download the version compatible with your Chrome browser (e.g., ChromeDriver version 114 for Chrome 114).

Extract the downloaded zip file and note the path to the chromedriver.exe.

Step 3: Create Project Structure
Create a directory for your project and organize it as follows:


project/
|-- tests/
|   |-- test_RegisterUser.py
|-- pageObjects/
|   |-- registerPage.py
|-- Reports/
|-- Screenshot/
|-- requirements.txt


Step 4: Code Implementation
registerPage.py
python
Copy code
# pageObjects/registerPage.py

from selenium import webdriver

class AddUser:
    rdMaleGender_id = "uniform-id_gender1"
    rdFeMaleGender_id = "uniform-id_gender2"
    textbox_signup_name = "Name"
    textbox_email_name = "email"
    # ... (other elements)

    def __init__(self, driver):
        self.driver = driver

    def set_gender(self, gender):
        if gender == 'Male':
            self.driver.find_element_by_id(self.rdMaleGender_id).click()
        elif gender == 'Female':
            self.driver.find_element_by_id(self.rdFeMaleGender_id).click()
        else:
            self.driver.find_element_by_id(self.rdMaleGender_id).click()

    # ... (other methods for setting form fields)
test_RegisterUser.py
python
Copy code
# tests/test_RegisterUser.py

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, WebDriverException
import logging
import time
from pageObjects.registerPage import AddUser

@pytest.fixture
def setup():
    # Specify the path to your chromedriver executable
    chromedriver_path = r'C:\path\to\chromedriver.exe'

    # Configure Chrome options
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')  # Optional: Run Chrome in headless mode

    # Initialize the Chrome driver with the specified path and options
    service = webdriver.chrome.service.Service(chromedriver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)

    yield driver

    # Close the browser after the test
    driver.quit()

class Test_002_RegisterUser:
    baseUrl = "http://automationexercise.com"
    signup_name = "New User"
    email_name = "newuser@example.com"
    password = "password123"
    gender = "Male"
    day = "15"
    month = "5"
    year = "1990"

    def test_register_new_user(self, setup):
        driver = setup
        driver.get(self.baseUrl)

        try:
            # Instantiate the AddUser object
            ru = AddUser(driver)

            # Fill in the registration form using updated method calls
            ru.set_gender(self.gender)
            # ... (set other form fields)

            # Submit the registration form
            # ... (submit form)

            # Assertions for successful registration
            # ... (assertions)

        except (TimeoutException, WebDriverException) as e:
            screenshot_name = f"./Screenshot/test_register_user_{int(time.time())}.png"
            driver.save_screenshot(screenshot_name)
            logging.error(f"Error during registration: {e}")
            raise
Step 5: Run the Test
Run the test by executing the following command in the terminal or command prompt:

bash
Copy code
pytest -s -v --html=Reports/report.html tests/test_RegisterUser.py
This command runs the test and generates an HTML report in the Reports directory.
