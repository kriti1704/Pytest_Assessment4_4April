from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):

    # locators
    login_link = (By.LINK_TEXT, "Log in")
    email = (By.ID, "Email")
    password = (By.ID, "Password")
    login_button = (By.XPATH, "//input[@value='Log in']")

    # initialize constructor
    def __init__(self, driver):
        super().__init__(driver) # call parent class constructor

    # click action
    def click_login(self):
        self.click(self.login_link)

    # entering email
    def enter_email(self, email):
        self.enter_text(self.email, email)

    #entering password
    def enter_password(self, password):
        self.enter_text(self.password, password)

    # clicking login button
    def click_login_button(self):
        self.click(self.login_button)