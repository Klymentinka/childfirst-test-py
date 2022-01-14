Feature: Signup page

  Scenario Outline: go to signup page
    Given we are on signup page
    When we enter <email> and <password> and <confirm password>
    And click "Sign up"
    Then we are on myinfo page

    Examples:
    | email             | password  | confirm password |
    | test12@email.com  | 1A4baby$  | 1A4baby$         |
    | testasd@email.com |123456     |  123456          |
  