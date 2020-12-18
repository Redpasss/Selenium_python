from selenium.webdriver.common.by import By
from lib.base_element import BaseElement
from lib.base_page import BasePage
from lib.locator import Locator


class WomenPage(BasePage):

    url = 'http://automationpractice.com/index.php?id_category=3&controller=category'

    def element(self, loc):
        locator = Locator(By.XPATH, loc)
        return BaseElement(driver=self.driver, locator=locator)


