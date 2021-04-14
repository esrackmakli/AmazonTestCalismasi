from selenium.webdriver.common.by import By
from BaseClass.base_class import BaseClass


class CategoryPage:
    SELECT_LAPTOP = (By.CLASS_NAME, "octopus-pc-category-card-v2-item")
    LAPTOP_SELECTED = (By.XPATH, "//h1[contains(text(),'Dizüstü Bilgisayarlar')]")
    text = "Dizüstü Bilgisayarlar"
    SELECT_PRODUCT = (By.CLASS_NAME, "octopus-pc-item")
    PRODUCT_SELECTED = (By.ID, "add-to-cart-button")

    def __init__(self, driver):
        self.driver = driver
        self.functions = BaseClass(self.driver)

    def click_laptop(self):
        """
        Navigates to the laptop category page and checks it

        """
        self.functions.wait_for_element(self.SELECT_LAPTOP).click()
        laptop_selected = self.functions.wait_for_element(self.LAPTOP_SELECTED)
        assert laptop_selected.text == self.text, "didn't selected laptop!"

    def click_first_product(self):
        """
        Navigates to the first product in laptop category page and checks it

        """
        self.functions.wait_for_element(self.SELECT_PRODUCT).click()
        product_selected = self.functions.wait_for_element(self.PRODUCT_SELECTED)
        assert product_selected.is_displayed(), "didn't selected product!"
