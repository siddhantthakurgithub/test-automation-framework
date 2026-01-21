import requests
from behave import given, when, then

@given("the users API endpoint is available")
def step_users_endpoint(context):
    # context.base_url comes from .env
    context.url = f"{context.base_url}/users"

@when("I send a GET request to fetch users")
def step_send_get_request(context):
    context.response = requests.get(context.url, headers=context.headers)

@then("the response status code should be 200")
def step_validate_status_code(context):
    assert context.response.status_code == 200, (
        f"Expected 200 but got {context.response.status_code}"
    )

@then("the response should contain a list of users")
def step_validate_users_list(context):
    response_json = context.response.json()

    assert isinstance(response_json, list), "Response is not a list"
    assert len(response_json) > 0, "Users list is empty"
    # Check that first user has common keys
    assert "id" in response_json[0], "User object missing 'id'"
    assert "email" in response_json[0], "User object missing 'email'"