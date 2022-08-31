from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group>a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    ITEM_IN_BASKET = (By.CSS_SELECTOR, ".basket-items")
    MESSAGE_ABOUT_EMPTY_BASKET = (By.CSS_SELECTOR, "#content_inner>p")

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")

    EMAIL_ADDRESS_LOG_IN = (By.NAME, "login-username")
    PASSWORD_LOG_IN = (By.NAME, "login-password")
    LOG_IN_BUTTON_SUBMIT = (By.NAME, "login_submit")

    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

    EMAIL_ADDRESS_REGISTER = (By.NAME, "registration-email")
    PASSWORD_REGISTER = (By.NAME, "registration-password1")
    PASSWORD_CONFIRM_REGISTER = (By.NAME, "registration-password2")
    REGISTER_BUTTON_SUBMIT = (By.NAME, "registration_submit")




class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.price_color:nth-child(2)')
    NAME_OF_PRODUCT = (By.CSS_SELECTOR, '.product_main > h1')

    MESSAGE_ABOUT_ADDING = (By.CSS_SELECTOR, 'div.alert:nth-child(1) strong')
    BASKET_PRICE = (By.CSS_SELECTOR, '.alertinner p strong')

    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages div:first-child")