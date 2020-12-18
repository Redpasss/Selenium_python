import os
import sys; sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from pages.vs_women import WomenPage
import json
import pytest


@pytest.mark.usefixtures("setup")
class TestAddToChartWomen:
    def test_add_to_cart_women(self):
        """Test the Add to cart button.
        Click on a Add to cart button opens alert window.
        Steps:
        1. Open the URL http://automationpractice.com/index.php?id_category=3&controller=category
        2. Maximize window
        3. Hover mouse over the product to get the Add to cart button
        4. Select the Add to cart button under listed product
        5. Click on the Add to cart button
        6. Check if the successfull adition to cart window apears
        7. Close the browser."""

        # Test setup:
        with open("../mystore.json") as f:
            data = json.load(f)
        hover = data["hover_element"]
        add_btn = data["add_button"]
        msg = data["msg"]


        # Actual test:
        women_page = WomenPage(self.driver)
        women_page.go()
        women_page.maximize_window()
        if self.driver.title == data["error_page"]:
            self.driver.refresh()
        else:
            women_page.element(hover).hover()
            women_page.element(add_btn).click()
            add_text = women_page.element(msg).text
            assert add_text == 'Product successfully added to your shopping cart'

