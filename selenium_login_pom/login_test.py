from selenium import webdriver
from pages.login_page import LoginPage
import time

def run_login_test(username, password):
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/login")
    driver.maximize_window()

    try:
        login_page = LoginPage(driver)
        login_page.login(username, password)

        time.sleep(2)

        if login_page.is_login_successful() and login_page.is_logout_present():
            print("Login successful")
        else:
            print("Login failed")
            print("Error:", login_page.get_flash_message())
            driver.save_screenshot("login_failure.png")
    except Exception as e:
        print("Exception occurred:", e)
        driver.save_screenshot("exception.png")
    finally:
        input("Press Enter to close browser...")
        driver.quit()

run_login_test("tomsmith", "SuperSecretPassword!")

run_login_test("invalid", "invalid")
