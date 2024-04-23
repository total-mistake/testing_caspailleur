Feature: Explore data functionality

  @explore_data
  Scenario: Exploring data
    Given I have a binary dataset
    When I explore the data
    Then I should get the expected results
