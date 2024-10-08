import os
import pytest
from core.load_secrets import get_secrets
import json
from core.driver_manager import get_driver
from pages.login_page import *


# yield driver
@pytest.fixture(scope="function")
def driver():
    driver = get_driver()
    yield driver
    driver.quit()


# login on startup fixture
@pytest.fixture(scope="function")
def login_on_startup(driver):
    login = LoginPage(driver=driver)
    username, password = get_secrets()
    yield login.login_on_startup(url="https://www.terminalx.com", username=username, password=password)