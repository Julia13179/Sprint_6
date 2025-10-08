import allure
from locators.home_page_locators import TestHomePageLocators as L
from pages.base_page import BasePage
from data import DZEN_URL


class HomePageSamokat(BasePage):

    @allure.step('Нажатие кнопки "Заказать" в хедере')
    def click_order_button_header(self):
        self.find_element_with_wait(L.ORDER_BUTTON_HEADER)
        self.click_on_element(L.ORDER_BUTTON_HEADER)

    @allure.step('Скролл до кнопки "Заказать" в теле страницы')
    def scroll_to_order_button_body(self):
        self.scroll_to_element(L.HOW_IT_WORKS_BLOCK)
        self.find_element_with_wait(L.ORDER_BUTTON_BODY)

    @allure.step('Нажатие кнопки "Заказать" в теле страницы')
    def click_order_button_body(self):
        self.click_on_element(L.ORDER_BUTTON_BODY)

    @allure.step('Закрытие окна куки')
    def close_cookie_window(self):
        self.find_element_with_wait(L.ACCEPT_COOKIE_BUTTON)
        self.click_on_element(L.ACCEPT_COOKIE_BUTTON)

    @allure.step('Скролл до блока "Вопросы о важном"')
    def scroll_to_faq(self):
        self.scroll_to_element(L.ACCORDION_BUTTON_FAQ_8)
        self.find_element_with_wait(L.ACCORDION_BUTTON_FAQ_8)

    @allure.step('Нажатие на вопрос')
    def click_the_question(self, question_locator):
        self.find_element_with_wait(question_locator)
        self.click_on_element(question_locator)

    @allure.step('Получение текста ответа')
    def get_the_answer_text(self, answer_locator):
        self.find_element_with_wait(answer_locator)
        answer = self.get_text_on_element(answer_locator)
        return answer

    @allure.step('Нажатие на логотип "Яндекс"')
    def click_logo_yandex_open_dzen_page(self):
        self.find_element_with_wait(L.LOGO_YANDEX)
        self.click_on_element(L.LOGO_YANDEX)
        self.switch_to_next_tab()
        self.wait_url_to_be(DZEN_URL)

    @allure.step('Нажатие на логотип "Самокат"')
    def click_logo_open_home_page(self):
        self.find_element_with_wait(L.LOGO_SAMOKAT)
        self.click_on_element(L.LOGO_SAMOKAT)

    @allure.step('Проверить URL Дзен')
    def check_dzen_url(self):
        return self.check_url(DZEN_URL)

    @allure.step('Проверить URL главной страницы')
    def check_home_url(self, base_url):
        return self.check_url(base_url)
