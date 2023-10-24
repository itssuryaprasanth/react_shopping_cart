Feature:  Add Items To Cart
  Scenario Outline: Verify user is able to add same items as desired
    Given Open Shopping Website In Chrome Browser
    When  Page is Loaded
    Then  Add Same item multiple times to cart from dashboard <Item>
    And   Click on Shopping cart
    Then  Verify items and prices in cart True
    And   Verify quantity of items in cart <Item>
    And   Sub total value in the cart None
    Then  Compare sub total value and items value <Item>
    Then  Increase items in the cart <Item>
    And   Verify quantity of items in cart 4
    And   Sub total value in the cart None
    And   Compare sub total value and items value <Item>
    And   Quit Shopping
    Examples:
      | Item |
      |  2   |

  Scenario:  Verify items are listed in cart in the order as added to cart with price
    Given Open Shopping Website In Chrome Browser
    When  Page is Loaded
    Then  Add Few items to cart with shipping label 2 True
    And   Add Few items to cart without shipping label 1 True
    And   Click on Shopping cart
    Then  Items to check in cart with free & without free shipping True
    And   Quit Shopping
