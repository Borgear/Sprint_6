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

    @allure.step("Прокрутка до элемента: {locator}")
    def scroll_to_element(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
    
    @allure.step("Ожидание и принятие куки")
    def wait_cookie_click(self, locator):
        self.click_element(locator)
    
    @allure.step("Ожидание появления в URL строки: {url_part}")
    def wait_for_url_contains(self, url_part):
        return WebDriverWait(self.driver, 10).until(EC.url_contains(url_part))