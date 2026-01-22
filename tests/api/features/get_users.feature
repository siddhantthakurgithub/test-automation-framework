@api @smoke
Feature: Users API validation

  @get_users
  Scenario: Get list of users
    Given the users API endpoint is available
    When I send a GET request to fetch users
    Then the response status code should be 200
    And the response should contain a list of users