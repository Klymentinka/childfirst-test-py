Feature: Signin page

  Scenario Outline: go to signin page
    Given we are on signin page
    When we enter <email> and <password>
    And click "Log in"
    Then we are on dashboard page

    Examples:
    | email             | password |
    | example@emai.com  | 1A4baby$ |
  