Feature: Buy Product


  Background:
    Given I Access to the Store


  @order
  Scenario Outline: Buy a Product
    When User <user> place the order for <product>
    And Complete the information with values <name> <country> <city> <ccard> <month> <year>
    And clicks on purchase button
    Then Message that purchase has been made is displayed
    Examples:
    | user | product | name | country | city | ccard | month | year |
    | User182 | Samsung galaxy s6 | Jose | Argentina | Cordoba| 4111111111111111 | February | 2024 |