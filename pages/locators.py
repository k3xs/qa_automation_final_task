from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")



class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.price_color:nth-child(2)')
    NAME_OF_PRODUCT = (By.CSS_SELECTOR, '.product_main > h1')

    MESSAGE_ABOUT_ADDING = (By.CSS_SELECTOR, 'div.alert:nth-child(1) strong')
    BASKET_PRICE = (By.CSS_SELECTOR, '.alertinner p strong')

    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages div:first-child")