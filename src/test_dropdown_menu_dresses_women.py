import json
import pytest
from selenium import webdriver
from pages.vs_women import WomenPage

@pytest.mark.unit()
def test_dropdown_menu_dresses():
    """Test the dropdown menu
       Click on + Dresses and open menu
       Steps:
       1. Open the URL http://automationpractice.com/index.php?id_category=3&controller=category
       2. Maximize window
       3. Click on menu Tops
       4. Check menu contains "Casual Dresses"
       5. Close the browser."""

    # Test Setup:
    driver = webdriver.Chrome(executable_path='C:/seleniumDrivers/chromedriver.exe')
    with open("../mystore.json") as f:
        data = json.load(f)


    # Actual test:
    women_page = WomenPage(driver=driver)
    women_page.go()
    women_page.maximize_window()
    if driver.title == data["error_page"]:
        driver.refresh()
    else:
        women_page.element(data["open_menu2"]).click()
        menu_txt = women_page.element(data["assert_dropdown_casual_dresses"]).text
        assert menu_txt == 'Casual Dresses'
        women_page.close()
