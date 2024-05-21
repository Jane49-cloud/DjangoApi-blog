from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import re

# Replace these with your actual details
email = "testuser@example.com"
new_password = "new_password123"

# Step 1: Set up the Selenium WebDriver
driver = webdriver.Chrome()
driver.maximize_window()

# Step 2: Navigate to the password reset request page
driver.get("http://127.0.0.1:8000/password/reset")

# Step 3: Enter the email and submit the form
email_input = driver.find_element(By.NAME, "email")
email_input.send_keys(email)
email_input.send_keys(Keys.RETURN)

# Step 4: Wait for the password reset email
# (In a real test, you might use an API to access the email inbox and fetch the reset link)
time.sleep(10)  # Wait for the email to be sent

# Simulate fetching the email and extracting the reset link
# Here, we manually provide the reset link for simplicity
reset_link = "http://127.0.0.1:8000/password/reset/confirm/OTcwNDYxMTI3NzY0NzM4MDQ5/c7ca80-3eb80467d62a0f7e18487be5367a2519"

# Step 5: Navigate to the password reset link
driver.get(reset_link)

# Step 6: Enter the new password and confirm it
new_password_input = driver.find_element(By.NAME, "new_password")
confirm_password_input = driver.find_element(By.NAME, "confirm_password")
new_password_input.send_keys(new_password)
confirm_password_input.send_keys(new_password)
confirm_password_input.send_keys(Keys.RETURN)

# Step 7: Wait for the confirmation message
try:
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//p[contains(text(), 'Password has been reset')]"))
    )
    print("Password reset successful")
except:
    print("Password reset failed")

# Close the browser
driver.quit()
