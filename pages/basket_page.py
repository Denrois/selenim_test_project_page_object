from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def no_items_in_basket(self):
        assert self.is_element_not_present(BasketPageLocators.ITEMS_IN_BASKET), \
            'Basket is not empty'

    def presence_of_empty_basket_message(self):
        assert self.is_element_present(BasketPageLocators.EMPTY_BASKET_MSG), \
            'No empty basket message'


