import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options as EdgeOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


def pytest_addoption(parser):
    # add browser command(--browser), set chrome browser by default
    parser.addoption('--browser', action='store', default='chrome',
                     help='chrome(default), firefox, edge')
    # add language command(--lang), set english by default
    parser.addoption('--lang', action='store', default='en-gb',
                     help='en-gb(default), ')


@pytest.fixture
def driver(request):
    browser_name = request.config.getoption('browser')
    user_language = request.config.getoption('lang')
    if browser_name == 'chrome':
        chrome_options = ChromeOptions()
        chrome_options.add_argument('headless')
        chrome_options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),
                                   options=chrome_options)
    elif browser_name == 'firefox':
        firefox_options = FirefoxOptions()
        firefox_options.add_argument('headless')
        firefox_options.set_preference('intl.accept_languages', user_language)
        browser = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()),
                                    options=firefox_options)
    elif browser_name == 'edge':
        edge_options = EdgeOptions()
        edge_options.add_argument('headless')
        edge_options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()),
                                 options=edge_options)
    else:
        raise pytest.UsageError('chrome, firefox, edge')
    yield browser
    browser.quit()
