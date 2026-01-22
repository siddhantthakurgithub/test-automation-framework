@ui @smoke
Feature: Google Search

  @search
  Scenario: Validate Google search works
    Given I open the Google homepage
    When I search for "Hello GHL"
    Then I should see results related to "Hello GHL"