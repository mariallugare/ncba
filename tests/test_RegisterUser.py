import pytest
from selenium import webdriver

@pytest.fixture
def setup():
    # Specify the path to your chromedriver executable
    chromedriver_path = r'C:\Users\Miss Lugare\Downloads\chromedriver_win32 (1)\chromedriver.exe'

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
    gender = "Male"  # Adjust as needed
    day = "15"
    month = "5"
    year = "1990"
    # ... (other registration details)

    def test_register_new_user(self, setup):
        driver = setup
        driver.get(self.baseUrl)

        try:
            # Your test code here
            pass

        except Exception as e:
            # Handle exceptions
            print(f"Error during registration: {e}")
            raise

        finally:
            # Close the browser after the test
            driver.quit()





