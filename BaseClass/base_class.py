from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BaseClass(object):
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 90)

    def wait_for_element(self, selector):
        """
        :param selector: Locator of desired item
        :return: Returns the clickable item found

        """
        return self.wait.until(ec.element_to_be_clickable(selector))

