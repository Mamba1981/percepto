from selenium import webdriver
import os


def get_driver():
    try:
        return __get_local_chrome()
    except Exception as e:
        print(f"Chrome browser not supported, could not load driver: {e}")


def __get_local_chrome():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    try:
        chrome_driver = webdriver.Chrome(options=options)
        return chrome_driver
    except Exception as e:
        print("Exception occurred while downloading chrome driver:", e)
        return None