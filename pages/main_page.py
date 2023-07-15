from .base_page import BasePage
from .locators import MainPageLocators


class MainPage(BasePage):
    def should_be_login_link(self):
        assert self.is_element_present(MainPageLocators.LOGIN_LINK)

    def go_to_login_link(self):
        self.browser.find_element(*MainPageLocators.LOGIN_LINK).click()
