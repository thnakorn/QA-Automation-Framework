from behave import given, when, then
from src.pages.sauce_login_page import SauceLoginPage
from src.pages.sauce_inventory_page import InventoryPage


@given("I am on the Sauce Demo login page")
def step_open_login(context):
    context.page = SauceLoginPage(context.browser)
    context.page.load()


@when('I log in to Sauce Demo with username "{username}" and password "{password}"')
def step_login(context, username, password):
    context.page.login(username, password)
    context.inventory = InventoryPage(context.browser)


@then("I should see the Sauce Demo inventory page")
def step_verify_inventory(context):
    assert context.inventory.is_loaded()
