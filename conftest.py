import time

import pytest
from selenium import webdriver
from constants import Constants
@pytest.fixture(params=["chrome"],scope="class")
def initialise_driver(request):
    driver=None
    if request.param == "chrome":
        driver = webdriver.Chrome()

    # elif request.param == "firefox":1
    #     driver = webdriver.Firefox()
    # elif request.param == "edge":
    #     driver = webdriver.Edge()
    else:
        print("Provide a valid browser name")
    print("Browser",request.param)
    driver.get(Constants.url)
    driver.maximize_window()
    driver.execute_script(f"document.body.style.zoom='70%'")
    request.cls.driver = driver
    yield driver
    driver.quit()