from selenium.webdriver.common.by import By


class HomePage:
    URL = "https://example.com"

    def __init__(self, driver):
        self.driver = driver
        self.header = (By.TAG_NAME, "h1")

    def load(self):
        self.driver.get(self.URL)

    def get_header_text(self):
        return self.driver.find_element(*self.header).text
