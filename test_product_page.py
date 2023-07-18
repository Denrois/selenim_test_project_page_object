import pytest
from .pages.product_page import ProductPage


def test_guest_can_add_product_to_basket(driver):
    """ 1. Open page http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear
        2. User can see 'add to basket' button
        3. Click on 'add to basket' button
        4. Solve the quiz in alert window and click 'ok'
        Expected result: user can see message of successful adding product to basket,
                         product name in this message is equal to the product name we added,
                         user can see message with the whole products price in basket,
                         products price in basket is equal to the product price we added """
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


@pytest.mark.skip
@pytest.mark.negative
def test_guest_cant_see_success_message_after_adding_product_to_basket(driver):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(driver, link)
    page.open()
    page.add_to_basket()
    page.success_msg_not_present()


@pytest.mark.negative
def test_guest_cant_see_success_message(driver):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(driver, link)
    page.success_msg_not_present()


@pytest.mark.skip
@pytest.mark.negative
def test_message_disappeared_after_adding_product_to_basket(driver):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(driver, link)
    page.add_to_basket()
    page.success_msg_is_disappear()
