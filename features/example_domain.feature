Feature: Example Domain
  As a visitor
  I want to open the About page
  So that I can verify the title

  Scenario: Verify about page title
    Given I open the about page
    When I check the page title
    Then title should be "Example Domain"

  Scenario: Verify header text on about page
    Given I open the about page
    When I check the header text
    Then header should be "Example Domain"
