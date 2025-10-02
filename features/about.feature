Feature: About page
  As a visitor
  I want to open the About page
  So that I can verify the title

  Scenario: Verify about page title
    Given I open the about page
    When I check the page title
    Then it should be "About Us"
