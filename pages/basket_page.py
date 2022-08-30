from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_empty_basket(self):
        assert self.is_not_element_present(
            *BasketPageLocators.ITEM_IN_BASKET
        ), "The basket is not empty."

    def should_be_message_about_empty_basket(self):
        assert self.is_element_present(
            *BasketPageLocators.MESSAGE_ABOUT_EMPTY_BASKET
        ), "The message that the basket is empty is missing."
