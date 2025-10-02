from selenium.webdriver.common.by import By


class SauceLoginPage:
    URL = "https://www.saucedemo.com/"

    def __init__(self, driver):
        self.driver = driver
        self.username_input = (By.ID, "user-name")
        self.password_input = (By.ID, "password")
        self.login_button = (By.ID, "login-button")

    def load(self):
        self.driver.get(self.URL)

    def login(self, username, password):
        """Logs in to Sauce Demo using the provided credentials."""
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.login_button).click()
