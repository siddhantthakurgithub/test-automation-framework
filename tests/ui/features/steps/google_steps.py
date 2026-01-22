from behave import given, when, then
from pages.google_page import GooglePage

@given("I open the Google homepage")
def step_open_google(context):
    context.google_page = GooglePage(context.driver, base_url=context.base_url)
    context.google_page.open()

@when('I search for "{query}"')
def step_search(context, query):
    context.google_page.search(query)

@then('I should see results related to "{query}"')
def step_validate_results(context, query):
    context.google_page.validate_results(query)