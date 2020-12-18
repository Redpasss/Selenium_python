from selenium import webdriver
from pages.vs_women import WomenPage
import json


def test_list_view():
    """Test the list view selection.
    Steps:
    1. Open the URL: http://automationpractice.com/index.php?id_category=3&controller=category
    2. Maximize window
    3. Select the list view button
    4. Click the list view button
    5. Check if the product display is changed
    6. Close the browser"""

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
        women_page.element(data["list_view"]).click()
        list_text = women_page.element(data["title_selector"]).text
        assert list_text == "Faded Short Sleeve T-shirts"
        women_page.close()




