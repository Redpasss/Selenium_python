import os
import time
import sys;sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from pages.vs_blouse import BlousePage
import json
import pytest



@pytest.mark.usefixtures("setup")
class TestSizeSelect:
    def test_size_select(self):
        """Test the Quantity option.
        Steps:
        1. Open the URL http://automationpractice.com/index.php?id_product=2&controller=product
        2. Maximize window
"""

        # Test setup:
        with open("../mystore.json") as f:
            data = json.load(f)
        size_select = data["size_select"]
        add_to_cart = data["add_to_cart"]
        in_cart_txt = ("//*[@id='layer_cart_product_attributes']")



        # Actual test:
        blouse_page = BlousePage(self.driver)
        blouse_page.go()
        blouse_page.maximize_window()
        if self.driver.title == data["error_page"]:
            self.driver.refresh()
        else:
            blouse_page.element(size_select).click()
            blouse_page.element(add_to_cart).click()
            items_in_cart = blouse_page.element(in_cart_txt).text
            assert items_in_cart == "Black, L"
            time.sleep(2)



