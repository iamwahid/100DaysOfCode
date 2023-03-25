import os

import pytest
from appium import webdriver


@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Remote(
        command_executor='http://0.0.0.0:4723/wd/hub',
        desired_capabilities={
            # 'app': os.path.expanduser('./android/app/build/outputs/apk/app-debug.apk'),
            'app': os.getcwd() + '/apps/ApiDemos-debug.apk',
            'platformName': 'Android',
            'deviceName': 'Android Emulator',
            'appActivity': '.app.SearchInvoke',
        },
    )

    yield driver  # Test code runs after this line

    # Teardown
    driver.quit()


def test_basic(driver):
    WAIT_SEC = 10
    driver.implicitly_wait(WAIT_SEC)

    elem = driver.find_element_by_accessibility_id('testview')

    assert elem is not None


def test_should_send_keys_to_search_box_and_then_check_the_value(driver):
    search_box_element = driver.find_element('txt_query_prefill')
    search_box_element.send_keys('Hello world!')

    on_search_requested_button = driver.find_element('btn_start_search')
    on_search_requested_button.click()

    search_text = driver.find_element('android:id/search_src_text')
    search_text_value = search_text.text

    assert 'Hello world!' == search_text_value
