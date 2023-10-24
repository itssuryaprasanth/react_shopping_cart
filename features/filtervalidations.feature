Feature: FilterValidations
  Scenario: Verify user is able to filter items using different size filters
    Given Open Shopping Website In Chrome Browser
    When  Page is Loaded
    Then  Apply Any Filter XS
    And   Fetch the product results found 1
    Then  Quit Shopping


  Scenario Outline: Verify user is able to apply multiple filters S,M at once
    Given Open Shopping Website In Chrome Browser
    When Page is Loaded
    Then Apply Any Filter S
    And Fetch Product title
    Then Unselect the filter S
    And Apply Any Filter M
    And Fetch Product title
    Then Unselect the filter M
    And Select multiple filters <Size>
    Then Verify the results of product titles after multiple filters
    And Quit Shopping
    Examples:
      | Size |
      | M,S |
