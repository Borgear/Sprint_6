import pytest
import allure
from data import ScooterTestData
from pages import MainPage, OrderPage
from locators import MainPageLocators
from urls import Urls

@allure.epic("Самокат: Заказ и Навигация")
class TestScooterOrderNav:
    @allure.feature("Заказ")
    @pytest.mark.parametrize("locator, data", [
        (MainPageLocators.UP_ORDER_BTN, ScooterTestData.USER_1), 
        (MainPageLocators.LOW_ORDER_BTN, ScooterTestData.USER_2)
    ])
    def test_order_flow(self, driver, locator, data):
        mp = MainPage(driver)
        op = OrderPage(driver)
        mp.click_order_button(locator)
        op.fill_order_form(data)
        assert "Заказ оформлен" in op.get_success_text()

    @allure.feature("Логотип скутер")
    def test_logo_scooter(self, driver):
        mp = MainPage(driver)
        mp.click_order_button(MainPageLocators.UP_ORDER_BTN)
        mp.click_element(MainPageLocators.LOGO_SCOOTER)
        assert driver.current_url == Urls.MAIN_PAGE_URL

    @allure.feature("Логотип Яндекс")
    def test_logo_yandex(self, driver):
        mp = MainPage(driver)
        mp.click_element(MainPageLocators.LOGO_YANDEX)
        driver.switch_to.window(driver.window_handles[-1])
        mp.wait_for_url_contains(Urls.DZEN_URL)
        assert Urls.DZEN_URL in driver.current_url
