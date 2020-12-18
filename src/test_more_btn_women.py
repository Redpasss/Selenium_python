from selenium import webdriver
import json
from pages.vs_women import WomenPage



def test_more_btn_women():
    """Test the button More
       Steps:
       1. Open the URL http://automationpractice.com/index.php?id_category=3&controller=category
       2. Maximize window
       3. Hover mouse on product
       4. Click on More button
       5. Make sure the new window is open
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
        women_page.element(data["more_btn"]).click()
        assert driver.title == "Faded Short Sleeve T-shirts - My Store"
        women_page.close()



