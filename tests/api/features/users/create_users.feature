@api @smoke
Feature: Create User API

  @create_user
  Scenario: Create a new user via POST
    Given the create user API endpoint is available
    When I send a POST request with user data
    Then the response status code should be 201
    And the response should contain the same user data