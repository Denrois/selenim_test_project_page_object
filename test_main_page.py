from .pages.main_page import MainPage
from .pages.login_page import LoginPage


def test_presence_of_login_link(driver):
    """ 1. Open main page http://selenium1py.pythonanywhere.com/
        Expected result: user can see 'login or register' link """
    link = 'http://selenium1py.pythonanywhere.com/'
    page = MainPage(driver, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page(driver):
    """ 1. Open main page
        2. Click on 'login or register' link
        Expected result: user can see login page http://selenium1py.pythonanywhere.com/accounts/login/
        with login and register forms """
    link = 'http://selenium1py.pythonanywhere.com/'
    page = MainPage(driver, link)
    page.open()
    page.go_to_login_link()
    login_page = LoginPage(driver, driver.current_url)
    login_page.should_be_login_page()


