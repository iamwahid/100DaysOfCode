import os

CHROME_DRIVER = "chrome_driver_init"
FIREFOX_DRIVER = "firefox_driver_init"

DRIVER_MAPPING = {"chrome": CHROME_DRIVER, "firefox": FIREFOX_DRIVER}
DRIVER_ENGINE = DRIVER_MAPPING[os.environ.get("DRIVER_ENGINE", 'chrome')]
