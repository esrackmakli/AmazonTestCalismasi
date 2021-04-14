import unittest
from selenium import webdriver
from PageClasses.main_page import MainPage
from BaseClass.base_class import BaseClass
from PageClasses.category_page import CategoryPage
from PageClasses.product_page import ProductPage
from PageClasses.cart_page import CartPage


class TestAmazon(unittest.TestCase):
    """Test case is:
          1. Go to given website
          2. Click to 'Bilgisayar' section
          3. Click to 'Diz Ustu Bilgisayar' category
          4. Click to first product in this category
          5. Click to add to cart button
          6. Go to cart page
          7. Increase the quantity of product
          8. Delete product

          """

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.base_class = BaseClass(self.driver)
        self.main_page = MainPage(self.driver)
        self.category_page = CategoryPage(self.driver)
        self.product_page = ProductPage(self.driver)
        self.cart_page = CartPage(self.driver)

    def test_amazon(self):
        self.main_page.load_website()
        self.main_page.click_computer()
        self.category_page.click_laptop()
        self.category_page.click_first_product()
        self.product_page.add_to_cart()
        self.product_page.go_to_cart()
        self.cart_page.increase_to_quantity()
        self.cart_page.delete_product()
