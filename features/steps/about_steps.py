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
