from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):

    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.REGISTER_FORM_EMAIL).send_keys(email)
        self.browser.find_element(*LoginPageLocators.REGISTER_FORM_PASS).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_FORM_CONFIRM_PASS).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON).click()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'accounts/login/' in self.browser.current_url, \
            'login url mismatch'

    def should_be_login_form(self):
        assert self.is_element_present(LoginPageLocators.LOGIN_FORM), \
            'can\'t find login form'

    def should_be_register_form(self):
        assert self.is_element_present(LoginPageLocators.REGISTER_FORM), \
            'can\'t find register form'
