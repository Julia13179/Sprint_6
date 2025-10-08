from selenium.webdriver.common.by import By

class TestOrderFormPageLocators:

    # --- Экран "Для кого самокат" ---
    FIRST_NAME_FIELD        = (By.XPATH, "//input[@placeholder='* Имя']")
    LAST_NAME_FIELD         = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_FIELD           = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_STATION_FIELD     = (By.XPATH, "//input[@placeholder='* Станция метро']")
    METRO_STATION_LIST      = (By.CSS_SELECTOR, ".select-search__select")
    SELECTED_STATION        = (By.XPATH, "//li[contains(@class,'select-search__row')][1]")

    PHONE_NUMBER_FIELD      = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    CONTINUE_BUTTON         = (By.XPATH, "//button[normalize-space()='Далее']")

    # --- Экран "Про аренду" ---
    TITLE_ABOUT_RENT_FORM   = (By.CSS_SELECTOR, ".Order_Header__BZXOb")

    RENTAL_DATE_FIELD       = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    CALENDAR                = (By.CSS_SELECTOR, ".react-datepicker__month-container")

    # Сегодняшняя и завтрашняя даты в календаре
   
    TOMORROW_DATE_CALENDAR = (By.XPATH, "//div[contains(@class,'react-datepicker__day--today')]/following-sibling::div[1]")
    TOMORROW_DATE_CALENDAR = (By.XPATH, "//div[contains(@class,'react-datepicker__day--today')]" "/following::div[contains(@class,'react-datepicker__day') " "and not(contains(@class,'outside'))][1]")

    # Поле и список "Срок аренды"
    RENTAL_DURATION_FIELD   = (By.XPATH, "//div[contains(@class,'Dropdown-placeholder') and contains(text(),'Срок аренды')]")
    RENTAL_DURATION_LIST    = (By.XPATH, "//div[contains(@class,'Dropdown-menu')]")
    DROPDOWN_ITEM_RENTAL_PERIOD = (By.XPATH, "//div[contains(@class,'Dropdown-menu')]//div[normalize-space()='трое суток']")
    RENTAL_DURATION_AFTER_INPUT = (By.XPATH, "//div[contains(@class,'Dropdown-placeholder') and contains(@class,'is-selected')]")

    # Цвет и комментарий
    CHOOSE_COLOR_FIELD      = (By.XPATH, "//div[normalize-space()='Цвет самоката']")
    CHECKBOX_GREY           = (By.ID, "grey")
    COMMENT_FIELD           = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")

    # Кнопка "Заказать"
    ORDER_BUTTON      = (By.XPATH, "//button[contains(@class,'Button_Middle__1CSJM') and normalize-space()='Заказать']")

    # --- Попапы ---
    POP_UP_CONFIRM_ORDER    = (By.XPATH, "//div[contains(@class,'Order_ModalHeader') and contains(.,'Хотите оформить заказ')]")
    YES_BUTTON_POP_UP_CONFIRM_ORDER = (By.XPATH, "//button[normalize-space()='Да']")
    POP_UP_COMPLETE_ORDER   = (By.XPATH, "//div[contains(@class,'Order_ModalHeader') and contains(.,'Заказ оформлен')]")

    MODAL_HEADER_ANY = (By.CSS_SELECTOR, "[class*='Order_ModalHeader']")
    

    