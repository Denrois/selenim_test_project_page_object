from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, element):
        try:
            assert self.browser.find_element(*element)
        except NoSuchElementException:
            return False
        return True

    def is_element_not_present(self, element, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(
                expected_conditions.presence_of_element_located(element))
        except TimeoutException:
            return True
        return False

    def is_element_disappear(self, element, timeout=4,):
        try:
            WebDriverWait(self.browser, timeout).until_not(
                expected_conditions.presence_of_element_located(element))
        except TimeoutException:
            return False
        return True

    def text_in_elements_match(self, first, second):
        first_element = self.browser.find_element(*first).text
        second_element = self.browser.find_element(*second).text
        return first_element == second_element
