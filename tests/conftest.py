import pytest
from selenium import webdriver
from urls import Urls
from locators import MainPageLocators
from pages import BasePage

@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get(Urls.MAIN_PAGE_URL)
    BasePage(driver).wait_cookie_click(MainPageLocators.COOKIE_BUTTON)
    yield driver
    driver.quit()
    