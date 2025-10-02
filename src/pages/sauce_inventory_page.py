from selenium.webdriver.common.by import By


class InventoryPage:
    URL = "https://www.saucedemo.com/inventory.html"

    def __init__(self, driver):
        self.driver = driver
        self.inventory_container = (By.ID, "inventory_container")
        self.first_add_to_cart = (By.CSS_SELECTOR, ".inventory_item button")
        self.cart_badge = (By.CLASS_NAME, "shopping_cart_badge")

    def is_loaded(self):
        return self.driver.current_url == self.URL and \
               self.driver.find_element(*self.inventory_container).is_displayed()

    def add_first_product(self):
        self.driver.find_element(*self.first_add_to_cart).click()

    def get_cart_count(self):
        return self.driver.find_element(*self.cart_badge).text
