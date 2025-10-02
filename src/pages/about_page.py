from selenium.webdriver.common.by import By


class AboutPage:
    URL = "https://example.com/about"

    def __init__(self, driver):
        self.driver = driver

    def load(self):
        self.driver.get(self.URL)

    def get_title(self):
        return self.driver.title

    def get_header_text(self):
        header = self.driver.find_element(By.TAG_NAME, "h1")
        return header.text
