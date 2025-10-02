from behave import given, then
import requests


@given("I send a request to the health endpoint")
def step_call_health(context):
    context.response = requests.get("https://api.publicapis.org/health")


@then("the response status should be 200")
def step_check_status(context):
    assert context.response.status_code == 200
