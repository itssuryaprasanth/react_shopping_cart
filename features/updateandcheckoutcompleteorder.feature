Feature: Update and checkout to complete order
  Scenario Outline: Verify user can delete items in cart
    Given Open Shopping Website In Chrome Browser
    When  Page is Loaded
    Then  Add Few Items to Cart <Items> True
    And   Verify total items in cart <Items>
    And   Click on Shopping cart
    Then  Verify items and prices in cart True
    Then  Remove product items from cart <Items>
    And   Products are not available in cart True
    Then  Sub total value in the cart <Value>
    And   Quit Shopping
    Examples:
      | Items | Value |
      | 2     | $0.00 |



  Scenario Outline:  Verify user is able to place order
    Given Open Shopping Website In Chrome Browser
    When  Page is Loaded
    Then  Add Few Items to Cart <Items> False
    And   Click on Shopping cart
    Then  Sub total value in the cart None
    And   Click on checkout in cart
    Then  Get Text from checkout alert message and verify sub total value is equal
    And   Accept checkout alert message
    And   Refresh Shopping page
    Then  Click on Shopping cart
    And   Products are not available in cart True
    Then  Quit Shopping
    Examples:
      | Items |
      | 2     |

