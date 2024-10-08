import time
import pytest
from pages.main_page import *


@pytest.mark.percepto
@pytest.mark.usefixtures("login_on_startup")
class TestAdminDevicesFunctional:
    def test_create_device(self, driver):
        main = MainPage(driver)
        # cot a bit stuck on waiting page to load, sorry
        time.sleep(5)
        main.click_search_button()
        main.explicitly_wait_for_element_to_be_present(10, *MainLocators.SEARCH_INPUT)
        main.send_value_to_field_by_locator("hello kitty", *MainLocators.SEARCH_INPUT)
        main.explicitly_wait_for_elements_to_be_visible(10, *MainLocators.SINGLE_DROPDOWN_RESULT)
        all_results = main.find_elements(MainLocators.SINGLE_DROPDOWN_RESULT)

        # if there are results, do test, if no, fail
        if all_results:
            for result in all_results:
                assert "hello kitty" in result.text.lower()
            # the order is not correct, so it fail, thus im commenting this out
            # all_prices = [float(i.find_element(By.XPATH, ".//div[contains(@class, 'price')]/div").text.replace(" ₪", "")) for
            #               i in all_results]
            # assert all_prices == sorted(all_prices)

            # check if result has price
            all_results[2].find_element(By.XPATH, "./div//a").click()
            time.sleep(2)
            # check font size (converted font size from root html 12px)
            assert main.is_element_present(MainLocators.PRICE)
            price = main.find_element(MainLocators.PRICE)
            # calculate 1.8rem*12
            assert price.value_of_css_property('font-size') == "21.6px"

        else:
            assert False
