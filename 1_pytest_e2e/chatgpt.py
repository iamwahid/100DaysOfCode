from selenium import webdriver

# Open the website in a Chrome browser
driver = webdriver.Chrome()
driver.get("https://env8.sejasa.com")

# Locate the login form elements
username_field = driver.find_element_by_id("username")
password_field = driver.find_element_by_id("password")
login_button = driver.find_element_by_id("login_button")

# Enter the login credentials
username_field.send_keys("testuser")
password_field.send_keys("testpass")

# Click the login button
login_button.click()

# Check if the login was successful by verifying that the user is redirected to the correct page
assert "https://env8.sejasa.com/dashboard" in driver.current_url

# Close the browser
driver.close()
