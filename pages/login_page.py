import time

from core.base_page import *
from locators.login_locators import *


class LoginPage(BasePage):

    def fill_email(self, email):
        try:
            self.send_value_to_field_by_locator(email, *LoginLocators.EMAIL_FIELD)
            time.sleep(0.3)
        except Exception as e:
            print(f"Could not fill email field: {e}")

    def fill_password(self, password):
        try:
            self.send_value_to_field_by_locator(password, *LoginLocators.PASSWORD_FIELD)
            time.sleep(0.3)
        except Exception as e:
            print(f"Could not fill password field: {e}")

    # is called by fixture
    def login_on_startup(self, url, username, password):
        self.driver.get(url)
        self.explicitly_wait_for_element_to_be_present(30, *LoginLocators.LOGIN_BTN)
        self.click_on_element(LoginLocators.LOGIN_BTN)
        self.fill_email(username)
        self.fill_password(password)
        try:
            self.find_element(LoginLocators.LOG_IN_BTN).click()
        except Exception as e:
            print(f"Could not click Log In Button: {e}")