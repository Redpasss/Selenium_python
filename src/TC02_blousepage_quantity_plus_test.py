import os
import sys;sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from pages.vs_blouse import BlousePage
import json
import pytest


@pytest.mark.usefixtures("setup")
class TestQuantityPlus:
    def test_quantity_change_plus(self):
        """Test the Quantity option.
        Steps:
        1. Open the URL http://automationpractice.com/index.php?id_product=2&controller=product
        2. Maximize window
        3. 

        7. Close the browser."""

        # Test setup:
        with open("../mystore.json") as f:
            data = json.load(f)
        quantity_plus = data["quantity_plus"]
        add_to_cart = data["add_to_cart"]
        in_cart_txt = ("//*[@id='layer_cart']/div[1]/div[2]/h2/span[1]")



        # Actual test:
        blouse_page = BlousePage(self.driver)
        blouse_page.go()
        blouse_page.maximize_window()
        if self.driver.title == data["error_page"]:
            self.driver.refresh()
        else:
            i = 0
            while i<4:
                i+=1
                blouse_page.element(quantity_plus).click()
            blouse_page.element(add_to_cart).click()
            items_in_cart = blouse_page.element(in_cart_txt).text
            assert items_in_cart == "There are 5 items in your cart."

