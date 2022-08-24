import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

LANGUAGES_LIST = ['ar', 'ca', 'cs', 'da', 'de',
                  'en', 'el', 'es', 'fi', 'fr',
                  'it', 'ko', 'nl', 'pl', 'pt',
                  'pt-br', 'ro', 'ru', 'sk', 'uk',
                  'zh-hans']


def pytest_addoption(parser):
    parser.addoption('--browser_name',
                     action='store',
                     default="chrome",
                     help="Choose browser: chrome or firefox")

    parser.addoption('--language',
                     action='store',
                     default='en',
                     help='Choose language: en, es, fr, ru ...')


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    browser = None
    user_language = request.config.getoption("language")

    if browser_name == "chrome" and user_language in LANGUAGES_LIST:
        print("\nstart chrome browser for test..")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox" and user_language in LANGUAGES_LIST:
        print("\nstart firefox browser for test..")
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language)
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox and --language should be es, fr, ru...")
    yield browser
    print("\nquit browser..")
    browser.quit()
