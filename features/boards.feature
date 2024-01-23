Feature: Board Test
@delete-board
  Scenario: Create Board
    When I create a new Board with name "Board-behave-Test"
    Then the board name should be "Board-behave-Test"
    And closed response value is "False"
@delete-board
  Scenario: Update Board
    Given I create a new Board with name "Board-update-Test"
    When I should be able to update the board name to "Board-behave-Test-updated"
    Then the board name should be "Board-behave-Test-updated"
    And closed response value is "False"


  Scenario: Delete Board
    Given I create a new Board with name "Board-delete-Test"
    When I deleted the board created
    Then check to verify if board was succesfully deleted
