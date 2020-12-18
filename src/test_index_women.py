from selenium import webdriver
from pages.vs_index import IndexPageVS
import json


def test_women_tab():
    """Test existance of the Women tab.
        This tab leads to the Women page.
        Steps:
        1. open URL: http://automationpractice.com/index.php
        2. Maximize window
        3. Click WOMEN tab on a top menu
        4. Check if the Title page is changed to expected
        5. Close the browser"""

    # Test Setup:
    driver = webdriver.Chrome(executable_path='C:/seleniumDrivers/chromedriver.exe')
    with open("../mystore.json") as f:
        data = json.load(f)


    # Actual test:
    index_page = IndexPageVS(driver=driver)
    index_page.go()
    index_page.maximize_window()
    if driver.title == data["error_page"]:
        driver.refresh()
    else:
        index_page.element(data["top_menu_women"]).click()
        assert driver.title == "Women - My Store"
        index_page.close()







