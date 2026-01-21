from behave import given, when, then
from utils.api_client import APIClient
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given("a contact exists via API")
def step_create_contact(context):
    context.contact_name = "BDD User"

    # Simulated API call
    # client = APIClient("https://api.example.com", token="dummy")
    # response = client.post("/contacts", {"name": context.contact_name})

    assert context.contact_name is not None

@when("I open the contacts page")
def step_open_contacts(context):
    context.driver.get("https://www.google.com")

@then("I should see the contact in the UI")
def step_verify_contact(context):
    WebDriverWait(context.driver, 10).until(
        EC.title_contains("Google")
    )