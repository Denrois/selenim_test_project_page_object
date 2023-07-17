import math
from selenium.common import NoAlertPresentException
from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET).click()

    def should_be_add_to_basket_button(self):
        assert self.is_element_present(ProductPageLocators.ADD_TO_BASKET), \
            'Can\'t find add to basket button'

    def should_be_product_add_to_basket_success_msg(self):
        assert self.is_element_present(ProductPageLocators.SUCCESS_MESSAGE), \
            'There is no adding to basket message'

    def product_name_match(self):
        assert self.text_in_element_match(ProductPageLocators.PRODUCT_NAME,
                                          ProductPageLocators.NAME_ADDED_TO_BASKET), \
            'Product name and product added to basket name mismatch'

    def product_price_match(self):
        assert self.text_in_element_match(ProductPageLocators.PRICE_BEFORE_ADDING,
                                          ProductPageLocators.PRICE_AFTER_ADDING), \
            'Product price and price in basket mismatch'

    def solve_the_quiz(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")