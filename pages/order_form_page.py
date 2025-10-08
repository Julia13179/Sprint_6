import allure
from datetime import date, timedelta
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from locators.order_form_page_locators import TestOrderFormPageLocators as L


class OrderFormPage(BasePage):
   
    @allure.step('Заполнить поле "Имя"')
    def set_first_name(self, name):
        self.set_text_to_elm(L.FIRST_NAME_FIELD, name)
        return self

    @allure.step('Заполнить поле "Фамилия"')
    def set_last_name(self, last_name):
        self.set_text_to_elm(L.LAST_NAME_FIELD, last_name)
        return self

    @allure.step('Заполнить поле "Адрес"')
    def set_address(self, address):
        self.set_text_to_elm(L.ADDRESS_FIELD, address)
        return self

    @allure.step('Заполнить поле "Метро"')
    def set_metro(self, station):
        
        self.click_on_element(L.METRO_STATION_FIELD)
        self.set_text_to_elm(L.METRO_STATION_FIELD, station)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(L.METRO_STATION_LIST))
        field = self.find_element_with_wait(L.METRO_STATION_FIELD)
        field.send_keys(Keys.DOWN, Keys.ENTER)
        return self

    @allure.step('Заполнить поле "Телефон"')
    def set_phone(self, number):
        self.set_text_to_elm(L.PHONE_NUMBER_FIELD, number)
        return self

    @allure.step('Нажать кнопку "Далее"')
    def click_next_button(self):
        self.click_on_element(L.CONTINUE_BUTTON)

    @allure.step('Проверка, что открылась форма "Про аренду"')
    def check_second_form_displayed(self):
        assert self.check_displaying_of_element(L.TITLE_ABOUT_RENT_FORM)

    @allure.step('Заполнить поле "Дата аренды" (завтрашним днём)')
    def set_rental_date(self):
        date_str = (date.today() + timedelta(days=1)).strftime("%d.%m.%Y")
        field = self.find_element_with_wait(L.RENTAL_DATE_FIELD)
        field.clear()
        field.send_keys(date_str, Keys.ENTER)
        return self
 
    @allure.step('Выбрать срок аренды "трое суток"')
    def set_rental_duration(self):
        self.click_on_element(L.RENTAL_DURATION_FIELD)
        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(L.RENTAL_DURATION_LIST))
        self.click_on_element(L.DROPDOWN_ITEM_RENTAL_PERIOD)
        return self
    
    @allure.step('Выбрать цвет (серый)')
    def set_color_field(self):
        self.click_on_element(L.CHECKBOX_GREY)
        return self

    @allure.step('Заполнить поле "Комментарий"')
    def set_comment_field(self, comment):
        self.set_text_to_elm(L.COMMENT_FIELD, comment)
        return self

    @allure.step('Нажать кнопку "Заказать"')
    def click_order_button(self):
        self.driver.switch_to.active_element.send_keys(Keys.ESCAPE)
        self.click_on_element(L.ORDER_BUTTON)
        WebDriverWait(self.driver, 15).until(EC.presence_of_element_located(L.POP_UP_CONFIRM_ORDER))
        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(L.YES_BUTTON_POP_UP_CONFIRM_ORDER))
        return self

    @allure.step('Подтвердить оформление заказа (кнопка "Да")')
    def click_yes_button_confirmation_pop_up(self):
        self.click_on_element(L.YES_BUTTON_POP_UP_CONFIRM_ORDER)
        WebDriverWait(self.driver, 15).until(lambda d: "оформлен" in d.find_element(*L.MODAL_HEADER_ANY).text.lower())
        return self

    @allure.step('Заполнить первую часть формы')
    def personal_information_input(self, name, last_name, address, station, number):
        self.set_first_name(name)\
            .set_last_name(last_name)\
            .set_address(address)\
            .set_metro(station)\
            .set_phone(number)
        self.click_next_button()
        self.check_second_form_displayed()

    @allure.step('Заполнить вторую часть формы')
    def rental_information_input(self, comment):
        self.set_rental_date()\
            .set_rental_duration()\
            .set_color_field()\
            .set_comment_field(comment)
        self.click_order_button()

