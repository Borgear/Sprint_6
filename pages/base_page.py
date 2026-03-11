import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Поиск элемента по локатору: {locator}")
    def find_element(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))

    @allure.step("Клик по элементу: {locator}")
    def click_element(self, locator):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))
        element.click()
    
    @allure.step("Получить текст элемента: {locator}")
    def get_text_from_element(self, locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        return element.text
    
    @allure.step("Прокрутка до элемента: {locator}")
    def scroll_to_element(self, locator):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
        self.driver.execute_script('arguments[0].scrollIntoView({block: "center", inline: "nearest"});', element)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))
    
    @allure.step("Ожидание и принятие куки")
    def wait_cookie_click(self, locator):
        self.click_element(locator)
    
    @allure.step("Переключиться на новую вкладку и дождаться URL: {expected_url}")
    def switch_to_new_window_and_wait_url(self, expected_url):
        WebDriverWait(self.driver, 10).until(lambda d: len(d.window_handles) > 1)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        WebDriverWait(self.driver, 10).until(EC.url_contains(expected_url))
    
    @allure.step("Получить текущий URL")
    def get_current_url(self):
        return self.driver.current_url
