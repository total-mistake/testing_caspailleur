Feature: Testing the base function

  @powerset
  Scenario: Calculate powerset of an iterable
    Given I have an iterable with elements
      | elements |
      | 1        |
      | 2        |
      | 3        |
    When I calculate the powerset
    Then I should get the expected powerset
      | powerset     |
      | {}           |
      | {1}          |
      | {2}          |
      | {3}          |
      | {1, 2}       |
      | {1, 3}       |
      | {2, 3}       |
      | {1, 2, 3}    |

  @subset
  Scenario: A set is a subset of another set
    Given the set
      |set      |
      |{1, 2, 3}|
    When I check if it's a subset of
      |set         |
      |{1, 2, 3}|
    Then I want the answer "true"


  @psubset
  Scenario:A set is a psubset of another set
    Given the set
      |set      |
      |{1, 2, 3}|
    When I check if it's a psubset of
      |set         |
      |{1, 2, 3}|
    Then I want the answer "false"


  @closure
  Scenario: Find columns describing the same rows
    Given the following true rows per column
      | Column Indices | True Rows       |
      | 0              | {0, 1, 3}       |
      | 1              | {0, 1, 2}       |
      | 2              | {0, 2}          |
      | 3              | {0, 1, 2, 3}    |
      | 4              | {}              |
    When I calculate the closure for description
      | description |
      | 1        |
      | 2        |
    Then I should get the expected closure
      | closure        |
      | 1              |
      | 2              |
      | 3              |