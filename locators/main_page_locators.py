from selenium.webdriver.common.by import By

class MainPageLocators:
    QUESTION = (By.ID, "accordion__heading-{}") # вопрос в выпадающем списке
    ANSWER = (By.ID, "accordion__panel-{}") # ответ в выпадающем списке
    UP_ORDER_BTN = (By.XPATH, ".//div[contains(@class, 'Header_Nav')]//button[text()='Заказать']") # верхняя кнопка заказать
    LOW_ORDER_BTN = (By.XPATH, ".//div[contains(@class, 'Home_FinishButton')]//button") #нижняя кнопка заказать
    LOGO_SCOOTER = (By.XPATH, ".//a[contains(@class, 'Header_LogoScooter')]") # логотип самоката
    LOGO_YANDEX = (By.XPATH, ".//a[contains(@class, 'Header_LogoYandex')]") # логотип Яндекс
    COOKIE_BUTTON = (By.ID, "rcc-confirm-button") # кнопка принять куки
