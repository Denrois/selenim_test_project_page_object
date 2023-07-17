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



