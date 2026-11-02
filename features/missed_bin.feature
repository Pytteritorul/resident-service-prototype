Feature: Report a missed bin collection
  As a council resident,
  I want to report a missed bin collection,
  So that the council can investigate and arrange for my bin to be collected.

  The service should accept valid reports and provide clear
  error messages when the information entered is invalid.

  Scenario: Successfully report a missed bin collection
    Given the resident provides their name "John Smith"
    And the resident provides their postcode "SW1A 1AA"
    And the resident selects the bin type "General Waste"
    And the resident provides the missed collection date "2026-10-30"
    When the resident submits the report
    Then the report should be accepted
    And a confirmation message should be displayed

  Scenario: Reject a report with an invalid postcode
    Given the resident provides their name "John Smith"
    And the resident provides their postcode "INVALID"
    And the resident selects the bin type "General Waste"
    And the resident provides the missed collection date "2026-10-30"
    When the resident submits the report
    Then the report should be rejected
    And an error message "Invalid postcode" should be displayed

  Scenario: Successfully report a missed recycling collection
    Given the resident provides their name "Sarah Jones"
    And the resident provides their postcode "E1 6AN"
    And the resident selects the bin type "Recycling"
    And the resident provides the missed collection date "2026-10-29"
    When the resident submits the report
    Then the report should be accepted
    And a confirmation message should be displayed