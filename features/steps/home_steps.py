from behave import given, when, then
from src.pages.home_page import HomePage


@given("I open the home page")
def step_open_home(context):
    context.page = HomePage(context.browser)
    context.page.load()


@when("I look at the header")
def step_check_header(context):
    context.header_text = context.page.get_header_text()


@then('I should see "Example Domain"')
def step_assert_header(context):
    assert "Example Domain" in context.header_text
