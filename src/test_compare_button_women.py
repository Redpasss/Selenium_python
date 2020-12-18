from selenium import webdriver
from pages.vs_women import WomenPage
import json
import time

def test_compare_button():
    """Test the Add to compare
       Steps:
       1. Open the URL http://automationpractice.com/index.php?id_category=3&controller=category
       2. Maximize window
       3. Hover mouse on product
       4. Click on Add to compare
       5. Check button Compare did it change value to 1
       6. Close the browser."""

    # Test setup:
    driver = webdriver.Chrome(executable_path='C:/seleniumDrivers/chromedriver.exe')
    with open("../mystore.json") as f:
        data = json.load(f)

    #Actual test:
    women_page = WomenPage(driver=driver)
    women_page.go()
    women_page.maximize_window()
    if driver.title == data["error_page"]:
        driver.refresh()
    else:
        women_page.element(data["image_selector"]).hover()
        women_page.element(data["add_to_compare"]).click()
        time.sleep(2)
        compare_value = women_page.element(data["compare_btn"]).text
        assert compare_value == "Compare (1)"
