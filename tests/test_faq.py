import pytest
import allure
from data import ScooterTestData
from pages import MainPage

@allure.epic("Самокат: FAQ")
class TestScooterFaq:
    @allure.feature("Выпадающий список")
    @pytest.mark.parametrize("index, expected", list(enumerate(ScooterTestData.FAQ_ANSWERS)))
    def test_faq_accordion(self, driver, index, expected):
        mp = MainPage(driver)
        mp.click_question(index)
        assert expected in mp.get_answer_text(index)
