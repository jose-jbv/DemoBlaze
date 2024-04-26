Feature: Search Product

  Background:
    Given I Access to the Store

  @product
  Scenario Outline: Search for a valid product
    When User search for a product <product>
    Then Product page is displayed <product>
    Examples:
      | product |
      | Samsung galaxy s6 |
      | Nokia lumia 1520  |

  @product-cart
  Scenario Outline: Add Product to Cart
    When User search for a product <product>
    And Product page is displayed <product>
    And User add the product to the cart
    And Product is added to the cart
    And User review his cart
    Then Product <product> is visible in his cart
    Examples:
      | product |
      | Samsung galaxy s6 |
      | Nokia lumia 1520  |