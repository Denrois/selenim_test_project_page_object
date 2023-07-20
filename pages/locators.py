from selenium.webdriver.common.by import By


class BasePageLocators:
    BASKET_LINK = (By.CSS_SELECTOR, '.basket-mini a.btn')
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    USER_ICON = (By.CSS_SELECTOR, '.icon-user')


class BasketPageLocators:
    EMPTY_BASKET_MSG = (By.CSS_SELECTOR, '#content_inner>p')
    ITEMS_IN_BASKET = (By.CSS_SELECTOR, '.basket-items')


class MainPageLocators:
    pass


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')
    REGISTER_FORM_EMAIL = (By.CSS_SELECTOR, '#id_registration-email')
    REGISTER_FORM_PASS = (By.CSS_SELECTOR, '#id_registration-password1')
    REGISTER_FORM_CONFIRM_PASS = (By.CSS_SELECTOR, '#id_registration-password2')
    REGISTER_BUTTON = (By.CSS_SELECTOR, '[name="registration_submit"]')


class ProductPageLocators:
    ADD_TO_BASKET = (By.CSS_SELECTOR, '.btn-add-to-basket')
    NAME_ADDED_TO_BASKET = (By.CSS_SELECTOR, '#messages div:nth-child(1) strong')
    PRODUCT_NAME = (By.CSS_SELECTOR, 'div h1')
    PRICE_BEFORE_ADDING = (By.CSS_SELECTOR, '.product_main p.price_color')
    PRICE_AFTER_ADDING = (By.CSS_SELECTOR, '.alertinner>p>strong')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '#messages .alert-success:nth-child(1) .alertinner')
