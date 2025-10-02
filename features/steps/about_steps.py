from behave import given, when, then
from src.pages.about_page import AboutPage


@given("I open the about page")
def step_open_about(context):
    context.page = AboutPage(context.browser)
    context.page.load()


@when("I check the page title")
def step_get_title(context):
    context.title = context.page.get_title()


@then('it should be "About Us"')
def step_assert_title(context):
    assert context.title == "About Us"


@when("I check the header text")
def step_get_header_text(context):
    context.header_text = context.page.get_header_text()


@then('it should be "Example Domain"')
def step_assert_header_text(context):
    assert context.header_text == "Example Domain"
