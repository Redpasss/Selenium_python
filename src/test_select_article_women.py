from selenium import webdriver
from pages.vs_women import WomenPage
import json


def test_select_article():
    """Test the Select article
       Click on item name opens new page with article.
       Steps:
       1. Open the URL http://automationpractice.com/index.php?id_category=3&controller=category
       2. Maximize window
       3. Click on product name
       4. Check if new page is open
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
        women_page.element(data["quick_selector"]).click()
        button_txt = women_page.element(data["button"]).text
        assert button_txt == 'Add to cart'



