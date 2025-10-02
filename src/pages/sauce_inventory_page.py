from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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
        """Click on the first 'Add to cart' button and wait for cart badge to appear"""
        wait = WebDriverWait(self.driver, 15)
        button = wait.until(EC.element_to_be_clickable(self.first_add_to_cart))
        button.click()

    def get_cart_count(self):
        """Wait until the cart badge is present and return its text"""
        wait = WebDriverWait(self.driver, 15)
        element = wait.until(EC.presence_of_element_located(self.cart_badge))
        return element.text
