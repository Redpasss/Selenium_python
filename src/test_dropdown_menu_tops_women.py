import json
import pytest
from pages.vs_women import WomenPage

@pytest.mark.usefixtures("setup")
class TestDropdownMenuTops:
    def test_dropdown_menu_tops(self):
        """Test the dropdown menu
           Click on + Tops and open menu
           Steps:
           1. Open the URL http://automationpractice.com/index.php?id_category=3&controller=category
           2. Maximize window
           3. Click on menu Tops
           4. Check menu contains "T-Shirts" and "Blouses"
           5. Close the browser."""

        # Test Setup:
        with open("../mystore.json") as f:
            data = json.load(f)


        # Actual test:
        women_page = WomenPage(self.driver)
        women_page.go()
        women_page.maximize_window()
        if self.driver.title == data["error_page"]:
            self.driver.refresh()
        else:
            assert self.driver.title == "Women - My Store"
            women_page.element(data["open_menu"]).click()
            dropdown_txt = women_page.element(data["assert_dropdown_tshirts"]).text
            assert dropdown_txt == 'T-shirts'
            dropdown_txt_b = women_page.element(data["assert_dropdown_blouses"]).text
            assert dropdown_txt_b == 'Blouses'








