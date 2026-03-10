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
        assert op.is_success_order_message_displayed()

    @allure.feature("Логотип скутер")
    def test_logo_scooter(self, driver):
        mp = MainPage(driver)
        mp.click_order_button(MainPageLocators.UP_ORDER_BTN)
        mp.click_element(MainPageLocators.LOGO_SCOOTER)
        assert mp.get_current_url() == Urls.MAIN_PAGE_URL

    @allure.feature("Логотип Яндекс")
    def test_logo_yandex(self, driver):
        mp = MainPage(driver)
        mp.click_element(MainPageLocators.LOGO_YANDEX)
        assert mp.check_yandex_redirect(Urls.DZEN_URL)
