Feature: Home page
  As a user
  I want to open the home page
  So that I can see the header

  Scenario: Verify home page header
    Given I open the home page
    When I look at the header
    Then I should see "Example Domain"
