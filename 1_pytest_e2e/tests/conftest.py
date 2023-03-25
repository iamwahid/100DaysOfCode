import sys
import time
from time import sleep

import pytest
from selenium import webdriver


# Fixture for Firefox
@pytest.fixture(scope="class")
def firefox_driver_init(request):
    ff_driver = webdriver.Firefox()
    request.cls.driver = ff_driver
    yield
    ff_driver.close()


# Fixture for Chrome
@pytest.fixture(scope="class")
def chrome_driver_init(request):
    chrome_driver = webdriver.Chrome()
    request.cls.driver = chrome_driver
    yield
    chrome_driver.close()
