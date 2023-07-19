from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    BASKET_LINK = (By.CSS_SELECTOR, '.basket-mini a.btn')


class BasketPageLocators:
    EMPTY_BASKET_MSG = (By.CSS_SELECTOR, '#content_inner>p')
    ITEMS_IN_BASKET = (By.CSS_SELECTOR, '.basket-items')


class MainPageLocators:
    pass


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')


class ProductPageLocators:
    ADD_TO_BASKET = (By.CSS_SELECTOR, '.btn-add-to-basket')
    PRODUCT_NAME = (By.CSS_SELECTOR, 'div h1')
    NAME_ADDED_TO_BASKET = (By.CSS_SELECTOR, '#messages div:nth-child(1) strong')
    PRICE_BEFORE_ADDING = (By.CSS_SELECTOR, '.product_main p.price_color')
    PRICE_AFTER_ADDING = (By.CSS_SELECTOR, '.alertinner>p>strong')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '#messages .alert-success:nth-child(1) .alertinner')
