from selenium.webdriver.common.by import By
from BaseClass.base_class import BaseClass


class ProductPage:
    ADD_TO_CART_BTN = (By.ID, "add-to-cart-button")
    PRODUCT_ADDED_TO_CART = (By.XPATH, "//h1[contains(text(),'Sepete Eklendi')]")
    text = "Sepete Eklendi"
    CART_BTN = (By.ID, "nav-cart")
    CART_PAGE = (By.XPATH, "//h1[contains(text(),'Alışveriş Sepeti')]")
    cart_text = "Alışveriş Sepeti"

    def __init__(self, driver):
        self.driver = driver
        self.functions = BaseClass(self.driver)

    def add_to_cart(self):
        """
        Adds product to the cart and check is it added successfully

        """
        self.functions.wait_for_element(self.ADD_TO_CART_BTN).click()
        product_added_to_cart = self.functions.wait_for_element(self.PRODUCT_ADDED_TO_CART)
        assert product_added_to_cart.text == self.text, "didn't added to cart product!"

    def go_to_cart(self):
        """
        Navigate to cart page and check is it added successfully

        """
        self.functions.wait_for_element(self.CART_BTN).click()
        cart_page = self.functions.wait_for_element(self.CART_PAGE)
        assert cart_page.text == self.cart_text, "didn't loaded cart page!"
