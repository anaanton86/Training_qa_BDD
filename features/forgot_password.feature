Feature: Forgot password feature

  @smoke
  Scenario: Validate error message for wrong email
    Given Sign in: I navigate to sign in page
    When Sign in: I click on forgot password
    When Forgot pass: I write my email "email.com"
    Then Forgot pass: I validate that send email button is disabled
    Then Forgot pass: I validate invalid email error is displayed

  @smoke
  Scenario: Validate send email button is enabled
    Given Sign in: I navigate to sign in page
    When Sign in: I click on forgot password
    When Forgot pass: I write my email "aaa@email.com"
    Then Forgot pass: I validate that send email button is enabled



