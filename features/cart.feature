Feature: Shopping cart
  As a customer
  I want to add a product to the cart
  So that I can purchase it later

  Scenario: Add product to cart
    Given I am logged in as "standard_user" with password "secret_sauce"
    When I add the first product to the cart
    Then the cart badge should show "1"
