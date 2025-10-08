from selenium.webdriver.common.by import By


class TestHomePageLocators:

    # Кнопка "Заказать" в хедере
    ORDER_BUTTON_HEADER = By.CLASS_NAME, 'Button_Button__ra12g'
    # Кнопка "Заказать" в теле страницы
    ORDER_BUTTON_BODY = By.CLASS_NAME, 'Button_Middle__1CSJM'
    # Блок "Как это работает"
    HOW_IT_WORKS_BLOCK = By.XPATH, '//div[text()="Как это работает"]'
    # Кнопка "Принять куки"
    ACCEPT_COOKIE_BUTTON = By.ID, 'rcc-confirm-button'

    # Блок FAQ
    # Вопрос 1
    ACCORDION_BUTTON_FAQ_1 = By.ID, 'accordion__heading-0'
    # Ответ 1
    ANSWER_FAQ_1 = By.CSS_SELECTOR, 'div[aria-labelledby="accordion__heading-0"]:not([hidden]) p'
    # Вопрос 2
    ACCORDION_BUTTON_FAQ_2 = By.ID, 'accordion__heading-1'
    # Ответ 2
    ANSWER_FAQ_2 = By.CSS_SELECTOR, 'div[aria-labelledby="accordion__heading-1"]:not([hidden]) p'
    # Вопрос 3
    ACCORDION_BUTTON_FAQ_3 = By.ID, 'accordion__heading-2'
    # Ответ 3
    ANSWER_FAQ_3 = By.CSS_SELECTOR, 'div[aria-labelledby="accordion__heading-2"]:not([hidden]) p'
    # Вопрос 4
    ACCORDION_BUTTON_FAQ_4 = By.ID, 'accordion__heading-3'
    # Ответ 4
    ANSWER_FAQ_4 = By.CSS_SELECTOR, 'div[aria-labelledby="accordion__heading-3"]:not([hidden]) p'
    # Вопрос 5
    ACCORDION_BUTTON_FAQ_5 = By.ID, 'accordion__heading-4'
    # Ответ 5
    ANSWER_FAQ_5 = By.CSS_SELECTOR, 'div[aria-labelledby="accordion__heading-4"]:not([hidden]) p'
    # Вопрос 6
    ACCORDION_BUTTON_FAQ_6 = By.ID, 'accordion__heading-5'
    # Ответ 6
    ANSWER_FAQ_6 = By.CSS_SELECTOR, 'div[aria-labelledby="accordion__heading-5"]:not([hidden]) p'
    # Вопрос 7
    ACCORDION_BUTTON_FAQ_7 = By.ID, 'accordion__heading-6'
    # Ответ 7
    ANSWER_FAQ_7 = By.CSS_SELECTOR, 'div[aria-labelledby="accordion__heading-6"]:not([hidden]) p'
    # Вопрос 8
    ACCORDION_BUTTON_FAQ_8 = By.ID, 'accordion__heading-7'
    # Ответ 8
    ANSWER_FAQ_8 = By.CSS_SELECTOR, 'div[aria-labelledby="accordion__heading-7"]:not([hidden]) p'
    # Логотип Яндекс
    LOGO_YANDEX = By.CLASS_NAME, "Header_LogoYandex__3TSOI"
    # Логотип Самокат
    LOGO_SAMOKAT = By.CLASS_NAME, "Header_LogoScooter__3lsAR"
