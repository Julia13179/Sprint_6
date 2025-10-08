import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from data import BASE_URL
from pages.home_page import HomePageSamokat
from pages.order_form_page import OrderFormPage



@pytest.fixture(scope="function")
def driver():
    opt = Options()
    opt.set_preference("privacy.trackingprotection.enabled", False)
    opt.set_preference("privacy.trackingprotection.pbmode.enabled", False)
    opt.set_preference("dom.security.https_only_mode", False)
    opt.set_preference("network.cookie.cookieBehavior", 0)
    opt.set_preference("dom.webnotifications.enabled", False)
    opt.set_preference("intl.accept_languages", "ru-RU,ru")
    service = Service()
    drv = webdriver.Firefox(service=service, options=opt)
    drv.set_window_size(1280, 1024)
    drv.get(BASE_URL)
    yield drv
    drv.quit()

@pytest.fixture
def home_page(driver):
    page = HomePageSamokat(driver)
    try:
        page.close_cookie_window()
    except Exception:
        pass
    return page

@pytest.fixture
def order_page(driver):
    return OrderFormPage(driver)