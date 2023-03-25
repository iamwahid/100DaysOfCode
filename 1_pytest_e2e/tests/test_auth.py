import sys
import time
from time import sleep

import pytest
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from .constants import DRIVER_ENGINE


@pytest.mark.usefixtures(DRIVER_ENGINE)
class BasicFormTest:
    def _assert_prep(self):
        for name, expected in self.elements['preparations'].items():
            assert expected == getattr(self.driver, name)
        time.sleep(1)

    def _fill_inputs(self, submit=True):
        _last_input = None
        for name, attrs in self.elements['inputs'].items():
            _input = self.driver.find_element(by=By.XPATH, value=attrs['xpath'])
            _input.send_keys(attrs['input'])
            _last_input = _input
            time.sleep(0.5)
        if submit:
            # Option 1 - Send ENTER
            _last_input.send_keys(Keys.RETURN)
            # Option 2
            # _last_input.submit()
            time.sleep(1)

    def _assert_result(self):
        time.sleep(5)
        for name, expected in self.elements['results'].items():
            assert expected == getattr(self.driver, name)
        time.sleep(1)

    def test_run(self):
        self.driver.get(self.base_url.format(path=self.path))
        self.driver.maximize_window()

        self._assert_prep()

        self._fill_inputs()

        self._assert_result()


class TestAuth(BasicFormTest):
    base_url = "https://simping.id/{path}"
    path = "login"
    payload = {
        "email": "email@example.com",
        "password": "dummy",
    }

    elements = {
        "preparations": {
            "title": "Login - Simping.id",
        },
        "inputs": {
            "email": {"xpath": "//input[@name='email']", "input": payload["email"]},
            "password": {"xpath": "//input[@name='password']", "input": payload["password"]},
        },
        "results": {"title": "Simping.id - Halaman Utama"},
    }
