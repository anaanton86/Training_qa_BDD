Feature: Sign up feature

#  @live
#  Scenario: Validate error message for invalid email
#    Given Sign in: I navigate to sign in page
#    When Sign in: I click on sign up link
#    When Sign up: I select personal option
#    When Sign up: I complete first and last name inputs
#    When Sign up: I complete email input "email.com"
#    Then Sign up: I validate error message is as expected "Please enter a valid email address."
#
#
#  @live
#  Scenario: Validate error message for existing email
#    Given Sign in: I navigate to sign in page
#    When Sign in: I click on sign up link
#    When Sign up: I select personal option
#    When Sign up: I complete first and last name inputs
#    When Sign up: I complete email input "itfactory.ro@gmail.com"
#    Then Sign up: I validate error message is as expected "e-mail address is already in use"

## sau punem in Background: pasii comuni


  @live
  Scenario Outline: Validate error message for existing email
    Given Sign in: I navigate to sign in page
    When Sign in: I click on sign up link
    When Sign up: I select personal option
    When Sign up: I complete first and last name inputs
    When Sign up: I complete email input "<email>"
    Then Sign up: I validate error message is as expected "<error>"

    Examples:
      | email                   | error                               |
      | email.com               | Please enter a valid email address. |
      | itfactory.ro@gmail.com  | e-mail address is already in use    |
