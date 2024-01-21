
class Login:
    textbox_signup_name = "Name"
    textbox_email_name = "email "
    button_login_xpath = "//button[normalize-space()='Signup']"
    
    link_logout_linktext = "logout"

    def __init__(self, driver):
        self.driver = driver


    def setSignUpName(self,signup_name):
        self.driver.find_element_by_name(self.textbox_signup_name).clear()
        self.driver.find_element_by_name(self.textbox_signup_name).send_keys(signup_name)


    def setEmailName(self,email_name):
        self.driver.find_element_by_name(self.textbox_email_name).clear()
        self.driver.find_element_by_name(self.textbox_email_name).send_keys(email_name)

    def setEmailName(self, email_name):
        self.driver.find_element_by_name(self.textbox_email_name).clear()
        self.driver.find_element_by_name(self.textbox_email_name).send_keys(email_name)

    def ClickLogin(self):
        self.driver.find_element_by_xpath(self.button_login_xpath).click()


    def ClickLogout(self):
        self.driver.find_element_by_link_text(self.link_logout_linktext).click()


