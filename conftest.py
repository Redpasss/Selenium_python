import pytest
from selenium import webdriver
driver = None


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")


@pytest.fixture(scope='class')
def setup(request):
    global driver
    browser_name = request.config.getoption("browser")
    if browser_name == "chrome":
        driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
    elif browser_name == "firefox":
        driver = webdriver.Firefox(executable_path="C:\\geckodriver.exe")
    elif browser_name == "edge":
        driver = webdriver.Edge(executable_path="C:\\msedgedriver.exe")

    request.cls.driver = driver
    yield
    driver.close()
