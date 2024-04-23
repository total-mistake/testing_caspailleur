Feature: Testing order functions

    Scenario: Sorting elements using topological sorting
        Given I have a sorted list of elements
        | elements |
        | {} |
        | {1} |
        | {2} |
        | {0, 1} |
        | {0, 1, 2} |
        When I perform a topological sort of a list using an order pattern
        | map |
        | 0 |
        | 1 |
        | 3 |
        | 4 |
        | 2 |
        Then I should get the sorted elements and their indices mapping
