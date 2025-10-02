Feature: API health check
  As a QA engineer
  I want to test the API health endpoint
  So that I can confirm the service is up

  Scenario: Verify API health returns status 200
    Given I send a request to the health endpoint
    Then the response status should be 200
