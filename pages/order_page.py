import allure
from pages.base_page import BasePage
from locators import OrderPageLocators

class OrderPage(BasePage):

    @allure.step("Заполнить всю форму заказа данными пользователя")
    def fill_order_form(self, data):
        with allure.step("Заполнение первой части формы: персональные данные"):
            self.find_element(OrderPageLocators.NAME).send_keys(data["name"])
            self.find_element(OrderPageLocators.SURNAME).send_keys(data["surname"])
            self.find_element(OrderPageLocators.ADDRESS).send_keys(data["address"])
            self.click_element(OrderPageLocators.METRO)
            self.click_element(OrderPageLocators.METRO_ITEM)
            self.find_element(OrderPageLocators.PHONE).send_keys(data["phone"])
            self.click_element(OrderPageLocators.NEXT_BTN)
        with allure.step("Заполнение второй части формы: детали аренды"):
            self.find_element(OrderPageLocators.DATE).send_keys(data["date"])
            self.click_element(OrderPageLocators.SELECTED_DAY)
            self.click_element(OrderPageLocators.PERIOD)
            self.click_element(OrderPageLocators.PERIOD_DAY)
            self.click_element(data["color"])
            self.find_element(OrderPageLocators.COMMENT).send_keys(data["comment"])
            self.click_element(OrderPageLocators.ORDER_BTN)
            self.click_element(OrderPageLocators.YES_BTN)

    @allure.step("Проверить, что окно успешного заказа отображается")
    def is_success_order_message_displayed(self):
        return self.find_element(OrderPageLocators.SUCCESS_TITLE).is_displayed()
    