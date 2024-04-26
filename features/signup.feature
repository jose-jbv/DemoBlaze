Feature: Sign Up

  Background:
    Given I Access to the Store

  @signup
  Scenario Outline: Create Valid User
    When I enter a non-existing username <user>
    And I enter a valid password <pwd>
    And Click on the Signup Button
    Then User should be created
    Examples:
      | user | pwd |
      | User00019 | test123 |

  @signup-invalid
  Scenario Outline: Validate Error Message
    When I enter an existing username <user>
    And I enter a password <pwd>
    And Click on the Signup Button
    Then Error Message should be displayed.
    Examples:
      | user | pwd |
      | User00001 | test123 |
      | User00002 | test123 |