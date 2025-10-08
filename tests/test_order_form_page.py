import allure
import pytest
from data import user_1, user_2
from locators.order_form_page_locators import TestOrderFormPageLocators as L

@allure.title('Позитивное оформление заказа через верхнюю и нижнюю кнопки')
@allure.description('Заполнение обеих частей формы, подтверждение и проверка окна "Заказ оформлен"')
@pytest.mark.parametrize("start_button,user", [
    ("header", user_1),
    ("body",   user_2),
])
def test_order_form_flow(home_page, order_page, start_button, user):
    name, last_name, address, station, number, comment = user

    # открыть форму
    if start_button == "header":
        home_page.click_order_button_header()
    else:
        home_page.click_order_button_body()

    # заполнить
    order_page.personal_information_input(name, last_name, address, station, number)
    order_page.rental_information_input(comment)

    # подтвердить
    order_page.click_yes_button_confirmation_pop_up()

    # проверить
    assert order_page.find_element_with_wait(L.POP_UP_COMPLETE_ORDER).is_displayed(), \
        'Окно "Заказ оформлен" не появилось'

