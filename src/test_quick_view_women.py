import json
from selenium import webdriver
from pages.vs_women import WomenPage


def test_quick_view():
    """Test the button More
       Steps:
       1. Open the URL http://automationpractice.com/index.php?id_category=3&controller=category
       2. Maximize window
       3. Hover mouse on product
       4. Click on More button
       5. Make sure the new window is open
       6. Close the browser."""

    # Test Setup:
    driver = webdriver.Chrome(executable_path='C:/seleniumDrivers/chromedriver.exe')
    assert_product = '//*[@id="product_reference"]'
    with open("../mystore.json") as f:
        data = json.load(f)


    # Actual test:
    women_page = WomenPage(driver=driver)
    women_page.go()
    women_page.maximize_window()
    if driver.title == data["error_page"]:
        driver.refresh()
    else:
        women_page.element(data["image_selector"]).hover()
        women_page.element(data["quick_view"]).click()
        driver.switch_to.frame(driver.find_element_by_xpath(data["iframe"]))
        assert_product_txt = women_page.element(assert_product).text
        assert assert_product_txt == 'Model demo_1'
        women_page.close()

