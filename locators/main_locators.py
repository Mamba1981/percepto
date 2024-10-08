from selenium.webdriver.common.by import By


class MainLocators:
    SEARCH_BUTTON = (By.CSS_SELECTOR, "button[data-test-id='qa-header-search-button']")
    SEARCH_INPUT = (By.CSS_SELECTOR, "input[data-test-id='qa-search-box-input']")
    HEADER = (By.XPATH, "//button[contains(@class, 'profile-button-new-menu')]")
    SINGLE_DROPDOWN_RESULT = (By.XPATH, "//div[contains(@class, 'container')]//div[contains(@class, 'results')]//li[contains(@class, 'container')]")
    PRICE = (By.CSS_SELECTOR, "div[data-test-id='qa-pdp-price-final']")
