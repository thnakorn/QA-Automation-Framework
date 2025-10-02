Feature: User login in Sauce Demo
  As a Sauce Demo customer
  I want to log in with valid credentials
  So that I can access the Sauce Demo inventory page

  Scenario: Successful login with standard_user
    Given I am on the Sauce Demo login page
    When I log in to Sauce Demo with username "standard_user" and password "secret_sauce"
    Then I should see the Sauce Demo inventory page
