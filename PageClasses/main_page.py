from selenium.webdriver.common.by import By
from BaseClass.base_class import BaseClass


class MainPage:
    website = "http://www.amazon.com.tr/"
    MAIN_PAGE_LOADED = (By.ID, "gw-layout")
    SELECT_COMPUTER = (By.LINK_TEXT, "Bilgisayar")
    COMPUTER_SELECTED = (By.XPATH, "//h1[contains(text(),'Bilgisayar')]")
    text = "Bilgisayar"

    def __init__(self, driver):
        self.driver = driver
        self.functions = BaseClass(self.driver)

    def load_website(self):
        """
        Navigates to the homepage and checks it

        """
        self.driver.get(self.website)
        main_page_loaded = self.functions.wait_for_element(self.MAIN_PAGE_LOADED)
        assert main_page_loaded.is_displayed(), "didn't loaded website!"

    def click_computer(self):
        """
        Navigates to computer category page and checks it

        """
        self.functions.wait_for_element(self.SELECT_COMPUTER).click()
        computer_selected = self.functions.wait_for_element(self.COMPUTER_SELECTED)
        assert computer_selected.text == self.text, "didn't selected computer!"
