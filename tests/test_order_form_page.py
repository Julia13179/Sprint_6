import allure
import pytest
from data import user_1, user_2


class TestOrderFormPage:

    @allure.title('Позитивное оформление заказа через верхнюю кнопку')
    @allure.description('Заполнение обеих частей формы через кнопку в хедере, подтверждение и проверка окна "Заказ оформлен"')
    def test_order_form_flow_header_button(self, home_page, order_page):
        name, last_name, address, station, number, comment = user_1

        # открыть форму через кнопку в хедере
        home_page.click_order_button_header()

        # заполнить
        order_page.personal_information_input(name, last_name, address, station, number)
        order_page.rental_information_input(comment)

        # подтвердить
        order_page.click_yes_button_confirmation_pop_up()

        # проверить
        assert order_page.check_order_completion_popup_displayed(), \
            'Окно "Заказ оформлен" не появилось'

    @allure.title('Позитивное оформление заказа через нижнюю кнопку')
    @allure.description('Заполнение обеих частей формы через кнопку в теле страницы, подтверждение и проверка окна "Заказ оформлен"')
    def test_order_form_flow_body_button(self, home_page, order_page):
        name, last_name, address, station, number, comment = user_2

        # открыть форму через кнопку в теле страницы
        home_page.click_order_button_body()

        # заполнить
        order_page.personal_information_input(name, last_name, address, station, number)
        order_page.rental_information_input(comment)

        # подтвердить
        order_page.click_yes_button_confirmation_pop_up()

        # проверить
        assert order_page.check_order_completion_popup_displayed(), \
            'Окно "Заказ оформлен" не появилось'

