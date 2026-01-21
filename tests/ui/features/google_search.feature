@ui
Feature: Google Search Functionality

Scenario: Validate Google search works
    Given I open the Google homepage
    When I search for "OpenAI"
    Then I should see results related to "OpenAI"