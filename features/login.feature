Feature: Login

  Background:
    Given I Access to the Store


    @login
    Scenario Outline: Login with valid user
      When I enter a registered user <user>
      And Enter a valid password <pwd>
      And Click on the log in button
      Then User <user> is logged into the page
      Examples:
      | user | pwd |
      | User182 | test123 |
      | User38 | test123 |


   @login-invalid
   Scenario Outline: Login with invalid user
      When I enter invalid user <user>
      And I enter a invalid password <pwd>
      And Click on the login button
      Then Error message is displayed
      Examples:
        | user | pwd |
        | User182 | test1234 |
