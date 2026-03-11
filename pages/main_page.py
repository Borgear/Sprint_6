import allure
from pages.base_page import BasePage
from locators import MainPageLocators

class MainPage(BasePage):
    @allure.step("Открыть вопрос в FAQ под индексом {index}")
    def click_question(self, index):
        method, locator_string = MainPageLocators.QUESTION
        loc = (method, locator_string.format(index))
        self.scroll_to_element(loc)
        self.click_element(loc)

    @allure.step("Получить текст ответа в FAQ под индексом {index}")
    def get_answer_text(self, index):
        method, locator_string = MainPageLocators.ANSWER
        loc = (method, locator_string.format(index))
        return self.get_text_from_element(loc)

    @allure.step("Нажать на выбранную кнопку заказа")
    def click_order_button(self, locator):
        self.scroll_to_element(locator)
        self.click_element(locator)
    
    @allure.step("Нажать на логотип 'Самокат'")
    def click_logo_scooter(self):
        self.click_element(MainPageLocators.LOGO_SCOOTER)

    @allure.step("Нажать на логотип 'Яндекс' и переключиться на новую вкладку")
    def check_yandex_redirect(self, expected_url):
        self.click_element(MainPageLocators.LOGO_YANDEX)
        self.switch_to_new_window_and_wait_url(expected_url)
        return expected_url in self.get_current_url()
    