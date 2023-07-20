import time
import pytest
from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage


class TestUserAddToBasketFromProductPage:
    @pytest.fixture(autouse=True)
    def setup(self, driver):
        link = 'http://selenium1py.pythonanywhere.com/accounts/login/'
        page = LoginPage(driver, link)
        page.open()
        page.register_new_user(f'{time.time()}@validmail.com', 'a1f7dAJK8')
        page.is_user_authorized()

    @pytest.mark.xfail
    def test_user_cant_see_success_message_after_adding_product_to_basket(self, driver):
        """ 1. Open product page http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/
            2. Click on add to basket button
            Expected result: test fail, due to the presence of successful message """
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
        page = ProductPage(driver, link)
        page.open()
        page.add_to_basket()
        page.success_msg_not_present()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, driver):
        """ 1. Open page http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear
            2. User can see 'add to basket' button
            3. Click on 'add to basket' button
            4. Solve the quiz in alert window and click 'ok'
            Expected result: 1. User can see message of successful adding product to basket
                             2. Product name in this message is equal to the product name we added
                             3. User can see message with the whole products price in basket
                             4. Products price in basket is equal to the product price we added """
        link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
        page = ProductPage(driver, link)
        page.open()
        page.should_be_add_to_basket_button()
        page.add_to_basket()
        page.solve_the_quiz()
        page.product_name_match()
        page.product_price_match()

@pytest.mark.need_review
def test_guest_can_add_product_to_basket(driver):
    """ 1. Open page http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear
        2. Guest can see 'add to basket' button
        3. Click on 'add to basket' button
        4. Solve the quiz in alert window and click 'ok'
        Expected result: 1. Guest can see message of successful adding product to basket
                         2. Product name in this message is equal to the product name we added
                         3. Guest can see message with the whole products price in basket
                         4. Products price in basket is equal to the product price we added """
    link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    page = ProductPage(driver, link)
    page.open()
    page.should_be_add_to_basket_button()
    page.add_to_basket()
    page.solve_the_quiz()
    page.product_name_match()
    page.product_price_match()


@pytest.mark.parametrize('promo', [el if el !=7 else pytest.param(el, marks=pytest.mark.xfail(
                                    reason='known bug with name mismatch in promo7')) for el in range(10)])
def test_guest_can_add_product_to_basket_with_0_to_9_promo(driver, promo):
    """ Repeat the previous test(test_guest_can_add_product_to_basket) 10 times
        with different promo codes(from promo0 to promo9)
        Expected result: all tests should pass, except test with promo7 """
    link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo}'
    page = ProductPage(driver, link)
    page.open()
    page.should_be_add_to_basket_button()
    page.add_to_basket()
    page.solve_the_quiz_simplified()
    page.product_name_match()
    page.product_price_match()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(driver):
    """ 1. Open product page http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/
        2. Click on add to basket button
        Expected result: test fail, due to the presence of successful message """
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(driver, link)
    page.open()
    page.add_to_basket()
    page.success_msg_not_present()


def test_guest_cant_see_success_message(driver):
    """ 1. Open product page http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/
        Expected result: test pass, due to the absence of successful message """
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(driver, link)
    page.success_msg_not_present()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(driver):
    """ 1. Open product page http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/
        2. Click on add to basket button
        Expected result: Test fail, successful message is not disappearing """
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(driver, link)
    page.add_to_basket()
    page.success_msg_is_disappear()


def test_guest_should_see_login_link_on_product_page(driver):
    """ 1. Open product page http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/
        Expected result: guest can see 'login or register' link """
    link = 'http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/'
    page = ProductPage(driver, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(driver):
    """ 1. Open product page http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/
        2. Click on 'login or register' link
        Expected result: guest can see login page http://selenium1py.pythonanywhere.com/accounts/login/
                         with login and register forms """
    link = 'http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/'
    page = ProductPage(driver, link)
    page.open()
    page.go_to_login_link()
    login_page = LoginPage(driver, driver.current_url)
    login_page.should_be_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(driver):
    """ 1. Open product page http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/
        2. Click on 'View Basket' button
        Expected result: 1. Basket is empty
                         2. Guest can see empty basket message """
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(driver, link)
    page.open()
    page.go_to_basket_link()
    basket_page = BasketPage(driver, driver.current_url)
    basket_page.no_items_in_basket()
    basket_page.presence_of_empty_basket_message()
