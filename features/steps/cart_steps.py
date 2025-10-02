from behave import given, when, then
from src.pages.sauce_login_page import SauceLoginPage as LoginPage
from src.pages.sauce_inventory_page import InventoryPage


@given('I am logged in as "{username}" with password "{password}"')
def step_login(context, username, password):
    login_page = LoginPage(context.browser)
    login_page.load()
    login_page.login(username, password)
    context.inventory = InventoryPage(context.browser)
    assert context.inventory.is_loaded()


@when("I add the first product to the cart")
def step_add_product(context):
    context.inventory.add_first_product()


@then('the cart badge should show "1"')
def step_verify_cart(context):
    count = context.inventory.get_cart_count()
    assert count == "1"
