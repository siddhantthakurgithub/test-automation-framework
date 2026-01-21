@ui @smoke
Feature: Contacts management

  @create_contact
  Scenario: Create a new contact
    Given user is authenticated via API
    When user creates a contact
    Then contact should appear in UI

  @delete_contact
  Scenario: Delete a contact
    Given user has an existing contact
    When user deletes the contact
    Then contact should not appear in UI