from selenium.webdriver.common.by import By


class LoginLocators:
    LOGIN_BTN = (By.CSS_SELECTOR, "button[data-test-id='qa-header-login-button']")
    EMAIL_FIELD = (By.ID, "qa-login-email-input")
    PASSWORD_FIELD = (By.ID, "qa-login-password-input")
    LOG_IN_BTN = (By.XPATH, "//div[contains(@class, 'buttons-section')]//button[contains(text(), 'התחברות')]")
    LOGIN_POPUP = (By.XPATH, "//div[contains(@class, 'fullscreen-overlay')][2]")