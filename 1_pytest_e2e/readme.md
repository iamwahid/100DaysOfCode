# OS Mac Big Sur 11.6

# geckodriver for Firefox

https://github.com/mozilla/geckodriver/releases/tag/v0.31.0

```
tar -xf geckodriver-v0.31.0-macos.tar.gz -C driver
export DRIVER_PATH=$(pwd)/driver
export PATH="$PATH:$DRIVER_PATH"
```

# chromedriver for Chrome/Chromium

https://chromedriver.chromium.org/downloads

```
unzip chromedriver_mac64.zip -d driver
xattr -d com.apple.quarantine driver/chromedriver
export DRIVER_PATH=./driver
export PATH="$PATH:$DRIVER_PATH"
```

# appium for Android

https://medium.com/@liheyse/how-to-do-end-to-end-e2e-testing-for-react-native-android-on-real-devices-using-python-appium-800cd6c62541
https://github.com/appium/appium/blob/master/sample-code/python/test/test_android_basic_interactions.py

Appium driver
https://github.com/appium/appium-for-mac/releases/tag/v0.4.1

Appium Desktop
https://github.com/appium/appium-desktop/releases/tag/v1.22.3-4

Verify Appium 
```
npm install -g appium-doctor
```


# Website to test 

- http://webdriveruniversity.com/index.html
