import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains as AC
from selenium.webdriver.support import expected_conditions as EC


class BaseElement:
    def __init__(self, driver, locator):
        self.driver = driver
        self.locator = locator
        self.web_element = None
        self.find()

    def find(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator=self.locator))
        self.web_element = element
        return None

    def click(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator=self.locator))
        element.click()
        return None

    def send_keys(self, input_txt):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator=self.locator))
        element.send_keys(input_txt)

    def hover(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator=self.locator))
        AC(self.driver).move_to_element(element).perform()
        return None

    @property
    def text(self):
        text = self.web_element.text
        return text

