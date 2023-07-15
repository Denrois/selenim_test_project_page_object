from .pages.main_page import MainPage
from .pages.login_page import LoginPage


def test_presence_of_login_link(driver):
    link = 'http://selenium1py.pythonanywhere.com/'
    page = MainPage(driver, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page(driver):
    link = 'http://selenium1py.pythonanywhere.com/'
    page = MainPage(driver, link)
    page.open()
    page.go_to_login_link()
    login_page = LoginPage(driver, driver.current_url)
    login_page.should_be_login_page()


