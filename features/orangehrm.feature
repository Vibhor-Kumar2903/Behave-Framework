Feature: OrangeHRM Logo
  Scenario: Logo Presence on OrangeHRM home page
    Given   Launch chrome brower
    When    open orangeHrm home page
    Then    verify that the logo present on page
    And     close browser
