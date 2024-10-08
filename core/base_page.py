from selenium.webdriver.remote.webdriver import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time


# a class for general functionality
class BasePage:

    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    def navigate_to_url(self, url):
        # navigates to a url passed
        try:
            self.driver.get(url)
        except WebDriverException as e:
            print(f"Selenium Exception: {e}")

    def click_on_element(self, locator):
        # click on an element. pass a locator.
        try:
            self.driver.find_element(*locator).click()
        except Exception as e:
            print(f"Failed to click on element {e}")

    def find_element(self, locator):
        # returns an element. If element not fount raises NoSuchElement exception
        try:
            return self.driver.find_element(*locator)
        except Exception as e:
            print(f"Could not locate element: {locator}: {e}")

    def find_elements(self, locator):
        # find elements by locator. returns a list of elements (empty list if none found)
        try:
            return self.driver.find_elements(*locator)
        except Exception as e:
            print(f"Could not locate elements: {locator}: {e}")

    def explicitly_wait_for_element_to_be_clickable(
        # wait for element to be clickable
            self, wait_time: float, *locator: tuple
    ):
        try:
            WebDriverWait(self.driver, wait_time).until(
                EC.element_to_be_clickable(locator)
            )
        except TimeoutException:
            print(f"Timed out waiting for element to be clickable: {locator}")
        except NoSuchElementException:
            print(f"Element not found: {locator}")
        except Exception as e:
            print(f"An unexpected error occurred: {str(e)}")

    def explicitly_wait_for_element_to_be_present(
        # wait for element to be present
            self, wait_time: float, *locator: tuple
    ):
        try:
            WebDriverWait(self.driver, wait_time).until(
                EC.presence_of_element_located(locator)
            )
        except TimeoutException:
            print(f"Timed out waiting for element to be present: {locator}")
        except NoSuchElementException:
            print(f"Element not found: {locator}")
        except Exception as e:
            print(f"An unexpected error occurred: {str(e)}")

    def explicitly_wait_for_element_to_be_visible(
        # wait for element to be visible
            self, wait_time: float, *locator: tuple
    ):
        try:
            WebDriverWait(self.driver, wait_time).until(
                EC.visibility_of_element_located(locator)
            )
        except TimeoutException:
            print(f"Timed out waiting for element to be visible: {locator}")
        except NoSuchElementException:
            print(f"Element not found: {locator}")
        except Exception as e:
            print(f"An unexpected error occurred: {str(e)}")

    def explicitly_wait_for_elements_to_be_visible(
            self, wait_time: float, *locator: tuple
    ):
        try:
            WebDriverWait(self.driver, wait_time).until(
                EC.visibility_of_all_elements_located(locator)
            )
        except TimeoutException:
            print(f"Timed out waiting for elements to be visible: {locator}")
        except NoSuchElementException:
            print(f"Elements not found: {locator}")
        except Exception as e:
            print(f"An unexpected error occurred: {str(e)}")

    def send_value_to_field_by_locator(self, value, *locator):
        # send text value to a locator
        time.sleep(0.5)
        try:
            element = self.find_element(locator)
            element.send_keys(value)
            time.sleep(0.5)
        except Exception as e:
            print(f"failed to send value to {locator}: {str(e)}")

    def is_element_present(self, locator) -> bool:
        # check if element is on the page. returns true/false
        self.driver.implicitly_wait(2)
        try:
            self.driver.find_element(*locator)
            return True
        except NoSuchElementException:
            return False
        finally:
            self.driver.implicitly_wait(2)
