from selenium import webdriver
import json
from pages.vs_women import WomenPage


def test_add_to_wish_list_no_login():
    """Test the Add to Wishlist
       Steps:
       1. Open the URL http://automationpractice.com/index.php?id_category=3&controller=category
       2. Maximize window
       3. Hover mouse on product
       4. Click on Add to WishList
       5. Check is error message present "You must be logged in to manage your wishlist."
       6. Close the browser."""

    # Test setup:
    driver = webdriver.Chrome(executable_path='C:/seleniumDrivers/chromedriver.exe')
    fancybox_txt = "//p[contains(text(),'You must be logged in to manage your wishlist.')]"
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
        women_page.element(data["add_to_wish"]).click()
        error = women_page.element(fancybox_txt).text
        assert error == "You must be logged in to manage your wishlist."
