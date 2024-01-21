from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pytest

@pytest.fixture
def setup():  # Ensure a colon after 'def setup():'
    chromedriver_path = "C:\\Users\\Miss Lugare\\Downloads\\chromedriver_win32 (1)\\chromedriver.exe"
    service = Service(chromedriver_path)
    driver = webdriver.Chrome(service=service)
    yield driver
    driver.quit()
