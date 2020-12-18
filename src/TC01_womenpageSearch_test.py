import os
import sys; sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from pages.vs_women import WomenPage
import json
import pytest


@pytest.mark.usefixtures("setup")
class TestSearch:
    def test_search(self):
        """Test the Search field.
        Steps:
        1. Open the URL http://automationpractice.com/index.php?id_category=3&controller=category
        2. Maximize window
        3. Select search field
        4. Enter text "Blouse"
        5. Click on search button
        6. Check is product Blouse displayed
        7. Close the browser."""

        # Test setup:
        with open("../mystore.json") as f:
            data = json.load(f)
        search = data["search"]
        search_btn = data["search_btn"]
        article = data["blouse_article"]

        # Actual test:
        women_page = WomenPage(self.driver)
        women_page.go()
        women_page.maximize_window()
        if self.driver.title == data["error_page"]:
            self.driver.refresh()
        else:
            women_page.element(search).send_keys("Blouse")
            women_page.element(search_btn).click()
            article_txt = women_page.element(article).text
            assert article_txt == "Blouse"
