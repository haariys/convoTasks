from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_input = (By.ID, "username")
        self.password_input = (By.ID, "password")
        self.login_button = (By.CSS_SELECTOR, "button.radius")
        self.logout_button = (By.CSS_SELECTOR, "a.button.secondary.radius")
        self.flash_message = (By.ID, "flash")

    def login(self, username, password):
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.login_button).click()

    def is_login_successful(self):
        return "secure" in self.driver.current_url

    def is_logout_present(self):
        return len(self.driver.find_elements(*self.logout_button)) > 0

    def get_flash_message(self):
        return self.driver.find_element(*self.flash_message).text
