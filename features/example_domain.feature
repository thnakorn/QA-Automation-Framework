Feature: Example Domain
  As a visitor
  I want to open the Example page
  So that I can verify the title and header text

  Scenario: Verify Example page title
    Given I open the Example page
    When I check the Example page title
    Then title should be "Example Domain"

  Scenario: Verify header on Example page
    Given I open the Example page
    When I check the Example header
    Then header should be "Fail Example Domain"
