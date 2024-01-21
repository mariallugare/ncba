import time
from selenium.webdriver.support.ui import Select

class AddUser:
    # Register new user
    rdMaleGender_id = "uniform-id_gender1"
    rdFeMaleGender_id = "uniform-id_gender2"
    textbox_signup_name = "Name"
    textbox_email_name = "email"  # Removed extra space
    txtPassword_id = "password"  # Corrected from extra spaces
    txtDobDay_id = "days"
    txtDobMonth_id = "months"
    txtDoby_id = "years"
    txtFirstName_id = "first_name"
    txtLastName_id = "last_name"
    txtCompanyName_id = "company"
    txtAddress1_id = "address1"
    txtAddress2_id = "address2"  # Corrected from duplicate txtAddress1_id
    txtCountryName_id = "country"
    txtStateName_id = "state"
    txtCityName_id = "city"
    txtZipcodeName_id = "zipcode"
    txtNumber_id = "mobile_number"
    txtCreateAccount_id = "Create Account"
    button_login_id = "your_button_id"  # Replace with the correct ID

    def __init__(self, driver):
        self.driver = driver

    def setGender(self, gender):
        if gender == 'Male':
            self.driver.find_element_by_id(self.rdMaleGender_id).click()
        elif gender == 'Female':
            self.driver.find_element_by_id(self.rdFeMaleGender_id).click()
        else:
            self.driver.find_element_by_id(self.rdMaleGender_id).click()

    def setSignUpName(self, signup_name):
        self.driver.find_element_by_name(self.textbox_signup_name).clear()
        self.driver.find_element_by_name(self.textbox_signup_name).send_keys(signup_name)

    def setEmailName(self, email_name):
        self.driver.find_element_by_name(self.textbox_email_name).clear()
        self.driver.find_element_by_name(self.textbox_email_name).send_keys(email_name)

    def setPassword(self, password):
        self.driver.find_element_by_id(self.txtPassword_id).send_keys(password)

    def setDobDay(self, days):
        self.driver.find_element_by_id(self.txtDobDay_id).send_keys(days)

    def setDobMonth(self, months):
        self.driver.find_element_by_id(self.txtDobMonth_id).send_keys(months)

    def setDoby(self, years):
        self.driver.find_element_by_id(self.txtDoby_id).send_keys(years)

    def setFirstName(self, first_name):
        self.driver.find_element_by_id(self.txtFirstName_id).send_keys(first_name)

    def setLastName(self, last_name):
        self.driver.find_element_by_xpath(self.txtLastName_id).send_keys(last_name)

    def setCompanyName(self, company):
        self.driver.find_element_by_xpath(self.txtCompanyName_id).send_keys(company)

    def setCountry(self, country):
        self.driver.find_element_by_id(self.txtCountryName_id).send_keys(country)

    def setStateName(self, state):
        self.driver.find_element_by_id(self.txtStateName_id).send_keys(state)

    def setCityName(self, city):
        self.driver.find_element_by_id(self.txtCityName_id).send_keys(city)

    def setZipCodeName(self, zipcode):
        self.driver.find_element_by_id(self.txtZipcodeName_id).send_keys(zipcode)

    def setNumber(self, mobile_number):
        self.driver.find_element_by_id(self.txtNumber_id).send_keys(mobile_number)

    def ClickCreateAccount(self):
        self.driver.find_element_by_id(self.txtCreateAccount_id).click()
