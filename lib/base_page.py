import pytest

class BasePage(object):

    url = None

    def __init__(self, driver):
        self.driver = driver

    def go(self):
        self.driver.get(self.url)

    def maximize_window(self):
        self.driver.maximize_window()

    def close(self):
        self.driver.close()

    def get_url(self):
        url = self.driver.current_url
        return url