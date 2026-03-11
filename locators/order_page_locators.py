from selenium.webdriver.common.by import By

class OrderPageLocators:
    NAME = (By.XPATH, ".//input[@placeholder='* Имя']") # поле имя
    SURNAME = (By.XPATH, ".//input[@placeholder='* Фамилия']") # поле фамилия
    ADDRESS = (By.XPATH, ".//input[@placeholder='* Адрес: куда привезти заказ']") # поле адрес
    METRO = (By.XPATH, ".//input[@placeholder='* Станция метро']") # выпадающий список метро
    METRO_ITEM = (By.XPATH, ".//li[@role='menuitem']") # элемент выпадающего списка метро
    PHONE = (By.XPATH, ".//input[@placeholder='* Телефон: на него позвонит курьер']") # номер телефона
    NEXT_BTN = (By.XPATH, ".//button[text()='Далее']") # кнопка далее
    DATE = (By.XPATH, ".//input[@placeholder='* Когда привезти самокат']") # дата 
    SELECTED_DAY = (By.XPATH, ".//div[contains(@class, 'day--selected')]") # выбрать дату
    PERIOD = (By.CLASS_NAME, "Dropdown-control") # выпадающий список аренды
    PERIOD_DAY = (By.XPATH, ".//div[text()='сутки']") # элемент выпадающего списка аренды
    COLOR_BLACK = (By.ID, "black") # чекбокс цвета самоката (черный)
    COLOR_GREY = (By.ID, "grey") # чекбокс цвета самоката (серый)
    COMMENT = (By.XPATH, ".//input[@placeholder='Комментарий для курьера']") # поле комментария для курьера
    ORDER_BTN = (By.XPATH, ".//div[contains(@class, 'Order_Buttons')]//button[text()='Заказать']") # кнопка заказать
    YES_BTN = (By.XPATH, ".//button[text()='Да']") # кнопка да
    SUCCESS_TITLE = (By.XPATH, ".//*[contains(text(), 'Заказ оформлен')]") # заголовок успешного бронирования
