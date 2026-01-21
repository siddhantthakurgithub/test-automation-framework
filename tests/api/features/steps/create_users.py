import requests
import json
from behave import given, when, then
import logging

@given("the create user API endpoint is available")
def step_api_endpoint(context):
    """
    Prepare the URL and payload for the POST request.
    """
    context.url = f"{context.base_url}/users"
    context.user_payload = {
        "name": "John Doe",
        "username": "johndoe",
        "email": "john.doe@example.com"
    }
    logging.info(f"Prepared POST endpoint: {context.url} with payload {context.user_payload}")

@when("I send a POST request with user data")
def step_send_post_request(context):
    """
    Send the POST request and store the response in context.
    """
    try:
        context.response = requests.post(
            context.url,
            headers=context.headers,
            data=json.dumps(context.user_payload)
        )
        logging.info(f"POST request sent to {context.url}")
    except Exception as e:
        logging.error(f"POST request failed: {e}")
        raise

@then("the response status code should be 201")
def step_validate_status_code(context):
    """
    Validate that the response status code is 201 (Created).
    """
    try:
        assert context.response.status_code == 201, (
            f"Expected 201 but got {context.response.status_code}"
        )
        logging.info(f"Status code validated: {context.response.status_code}")
    except AssertionError as e:
        logging.error(f"Status code validation failed: {e}")
        logging.error(f"Response body: {context.response.text}")
        raise

@then("the response should contain the same user data")
def step_validate_response(context):
    """
    Ensure the response body matches the data we sent.
    """
    try:
        response_json = context.response.json()
        for key in context.user_payload:
            assert response_json[key] == context.user_payload[key], (
                f"Expected {key}={context.user_payload[key]}, got {response_json[key]}"
            )
        logging.info(f"Response validated successfully: {response_json}")
    except Exception as e:
        logging.error(f"Response validation failed: {e}")
        logging.error(f"Response body: {context.response.text}")
        raise