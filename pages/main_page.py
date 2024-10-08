from core.base_page import *
from locators.main_locators import *


class MainPage(BasePage):
    def click_search_button(self):
        try:
            self.click_on_element(MainLocators.SEARCH_BUTTON)
        except Exception as e:
            print(f"Could not click search button: {str(e)}")