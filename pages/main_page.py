import allure
from pages.base_page import BasePage
from locators import MainPageLocators

class MainPage(BasePage):
    @allure.step("Открыть вопрос в FAQ под индексом {index}")
    def click_question(self, index):
        loc = (MainPageLocators.QUESTION[0], MainPageLocators.QUESTION[1].format(index))
        self.scroll_to_element(loc)
        self.click_element(loc)

    @allure.step("Получить текст ответа в FAQ под индексом {index}")
    def get_answer_text(self, index):
        loc = (MainPageLocators.ANSWER[0], MainPageLocators.ANSWER[1].format(index))
        return self.find_element(loc).text

    @allure.step("Нажать на выбранную кнопку заказа")
    def click_order_button(self, locator):
        self.scroll_to_element(locator)
        self.click_element(locator)
