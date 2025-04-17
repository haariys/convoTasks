from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/upload")

file_path = os.path.abspath("sample.txt")

driver.find_element(By.ID, "file-upload").send_keys(file_path)
driver.find_element(By.ID, "file-submit").click()

time.sleep(1)
uploaded_name = driver.find_element(By.ID, "uploaded-files").text
if "sample.txt" in uploaded_name:
    print("ile upload verified")
else:
    print("Upload failed")

input("Press Enter to exit...")
driver.quit()
