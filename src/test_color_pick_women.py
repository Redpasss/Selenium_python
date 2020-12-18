from selenium import webdriver
import json
from pages.vs_women import WomenPage



def test_color_pick_women():
    """Test the select color
       Steps:
       1. Open the URL http://automationpractice.com/index.php?id_category=3&controller=category
       2. Maximize window
       3. Hover mouse on product
       4. Click on blue color button
       5. Make sure the new window is open with blue color products
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
        women_page.element(data["blue_color"]).click()
        url = women_page.get_url()
        assert url == 'http://automationpractice.com/index.php?id_product=1&controller=product#/size-s/color-blue'
        women_page.close()








