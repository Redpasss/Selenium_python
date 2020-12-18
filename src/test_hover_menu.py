import json
from selenium import webdriver
from pages.vs_index import IndexPageVS


def test_hover_menu():
    """Test of hover menu.
        Steps:
        1. open URL: http://automationpractice.com/index.php
        2. Maximize window
        3. Hover on menu button Women
        4. Check if menu is open
        5. Close the browser"""

    # Test Setup:
    driver = webdriver.Chrome(executable_path='C:/seleniumDrivers/chromedriver.exe')
    with open("../mystore.json") as f:
        data = json.load(f)


    # Actual test:
    index_page = IndexPageVS(driver=driver)
    index_page.go()
    driver.maximize_window()
    if driver.title == data["error_page"]:
        driver.refresh()
    else:
        index_page.element(data["top_menu_women"]).hover()
        selector_text = index_page.element(data["tops_xpath"]).text
        assert selector_text == "Blouses"
        driver.close()
