from selenium.webdriver.common.by import By
from BaseClass.base_class import BaseClass


class CartPage:
    DROPDOWN = (By.ID, "a-autoid-0")
    QUANTITY_SELECT = (By.ID, "dropdown1_2")
    CART_MESSAGE = (By.CLASS_NAME, "sc-quantity-update-message")
    DELETE_BTN = (By.CLASS_NAME, "a-color-link")
    PRODUCT_DELETED = (By.XPATH, "//h2[contains(text(),'Amazon Sepetiniz boş')]")
    text = "Amazon Sepetiniz boş"

    def __init__(self, driver):
        self.driver = driver
        self.functions = BaseClass(self.driver)

    def increase_to_quantity(self):
        """
        Clicks dropdown and increase the quantity and checks it

        """
        self.functions.wait_for_element(self.DROPDOWN).click()
        self.functions.wait_for_element(self.QUANTITY_SELECT).click()
        cart_message = self.functions.wait_for_element(self.CART_MESSAGE)
        assert cart_message.is_displayed(), "the quantity couldn't be increased!"

    def delete_product(self):
        """
        Delete the product that added to cart and checks it

        """
        self.functions.wait_for_element(self.DELETE_BTN).click()
        product_deleted = self.functions.wait_for_element(self.PRODUCT_DELETED)
        assert product_deleted.text == self.text, "didn't deleted product!"
