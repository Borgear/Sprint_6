import allure
from pages.base_page import BasePage
from locators import MainPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage(BasePage):
    @allure.step("Открыть вопрос в FAQ под индексом {index}")
    def click_question(self, index):
        loc = (MainPageLocators.QUESTION[0], MainPageLocators.QUESTION[1].format(index))
        self.scroll_to_element(loc)
        self.click_element(loc)

    @allure.step("Получить текст ответа в FAQ под индексом {index}")
    def get_answer_text(self, index):
        loc = (MainPageLocators.ANSWER[0], MainPageLocators.ANSWER[1].format(index))
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc)).text
        return self.find_element(loc).text

    @allure.step("Нажать на выбранную кнопку заказа")
    def click_order_button(self, locator):
        self.scroll_to_element(locator)
        self.click_element(locator)
    @allure.step("Нажать на логотип 'Самокат'")
    def click_logo_scooter(self):
        self.click_element(MainPageLocators.LOGO_SCOOTER)

    @allure.step("Нажать на логотип 'Яндекс' и переключиться на новую вкладку")
    def check_yandex_redirect(self, expected_url):
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.wait_for_url_contains(expected_url)
        return expected_url in self.get_current_url()
    