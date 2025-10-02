from selenium.webdriver.common.by import By


class SauceInventoryPage:
    URL = "https://www.saucedemo.com/inventory.html"

    def __init__(self, driver):
        self.driver = driver
        self.inventory_container = (By.ID, "inventory_container")

    def is_loaded(self):
        """Checks if the Sauce Demo inventory page is loaded."""
        return self.driver.current_url == self.URL and \
            self.driver.find_element(*self.inventory_container).is_displayed()
