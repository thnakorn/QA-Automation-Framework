from behave import given, when, then
from src.pages.about_page import AboutPage


@given("I open the Example page")
def step_open_example(context):
    context.page = AboutPage(context.browser)
    context.page.load()


@when("I check the Example page title")
def step_get_title(context):
    context.title = context.page.get_title()


@then('title should be "{title}"')
def step_assert_title(context, title):
    assert context.title == title


@when("I check the Example header")
def step_get_header_text(context):
    context.header_text = context.page.get_header_text()
    print("Header text: " + context.header_text)


@then('header should be "{header_text}"')
def step_assert_header_text(context, header_text):
    assert context.header_text == header_text
