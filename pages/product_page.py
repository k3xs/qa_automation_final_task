from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_add_to_basket_button(self):
        assert self.browser.find_element(
            *ProductPageLocators.ADD_TO_BASKET_BUTTON), "Add to basket button not presented"

    def should_be_name_of_product(self):
        assert self.browser.find_element(
            *ProductPageLocators.NAME_OF_PRODUCT), "Name of product not found"

    def should_be_price_of_product(self):
        assert self.browser.find_element(
            *ProductPageLocators.PRODUCT_PRICE), "Product Price not found"

    def should_be_msg_about_adding(self):
        # Проверка выхода сообщения что товар добавлен
        product_name = self.browser.find_element(*ProductPageLocators.NAME_OF_PRODUCT).text
        message = self.browser.find_element(*ProductPageLocators.MESSAGE_ABOUT_ADDING).text

        assert product_name == message, "Product name not found in message"

    def compare_basket_and_product_price(self):
        # Сравнение цен товара и пустой корзины
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        basket_price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text

        assert product_price == basket_price, "Product price and basket price is not equal"

    def add_product_to_basket(self):
        """
        Проверка нажатия на кнопку ADD_TO_BASKET_BUTTON
        Ожидаемый результат:
        1)Сообщение о том, что товар добавлен в корзину. Название товара в сообщении должно совпадать с тем товаром, который вы действительно добавили.
        2)Сообщение со стоимостью корзины. Стоимость корзины совпадает с ценой товара.
        """
        self.should_be_name_of_product()
        self.should_be_price_of_product()
        self.should_be_add_to_basket_button()

        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()

        self.solve_quiz_and_get_code()
        self.should_be_msg_about_adding()
        self.compare_basket_and_product_price()

    def should_not_be_success_message(self):
        assert self.is_not_element_present(
            *ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"

    def should_be_disappeared_element(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is not disappeared"
