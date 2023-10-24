from pytest_bdd import given, when, then, scenario, parsers
from features.common_steps.common_steps import ShoppingSteps
import pytest
import allure

"""

Test Scenario :

Filter Validations

"""


@allure.title("Verify user is able to filter items using different size filters XS, S, M, etc. and can see the "
              "results as expected")
@scenario('filtervalidations.feature', 'Verify user is able to filter items using different size filters')
def test_filter_validations_test_1():
    pass


@given("Open Shopping Website In Chrome Browser")
def launch_browser():
    pytest.shop_steps = ShoppingSteps()
    pytest.shop_steps.react_open_shopping_website_in_browser()


@when("Page is Loaded")
def verify_page_is_loaded():
    pytest.shop_steps.react_shopping_page_is_loaded()


@then(parsers.parse("Select multiple filters {size}"))
@then(parsers.parse("Apply Any Filter {size}"))
def apply_any_size_filter(size):
    if str(size).find(',') != -1:
        size_filter_with_list = size.split(',')
        for _ in size_filter_with_list:
            pytest.shop_steps.react_apply_which_any_size_filter(_)
    else:
        pytest.shop_steps.react_apply_which_any_size_filter(size)


@then(parsers.parse("Fetch the product results found {results}"))
def fetch_product_results(results):
    actual_result = pytest.shop_steps.react_fetch_product_results_found(results)
    try:
        if actual_result is False:
            raise AssertionError("Products results are not matching with search results..")
    finally:
        quit_browser()


@then('Quit Shopping')
def quit_browser():
    pytest.shop_steps.react_quit_shopping()


@allure.title("Verify user is able to apply multiple filters (S, M) at once and can see the results as expected ")
@scenario('filtervalidations.feature', 'Verify user is able to apply multiple filters S,M at once')
def test_filter_validations_test_2():
    pass


@then('Fetch Product title')
def fetch_product_title():
    pytest.shop_steps.react_fetch_product_title()


@then(parsers.parse("Unselect the filter {size}"))
def unselect_the_filter(size):
    apply_any_size_filter(size)


@then("Verify the results of product titles after multiple filters")
def verify_results_of_product_titles_after_multiple_filters():
    pytest.shop_steps.react_verify_product_titles_after_applying_multiple_filters()


"""

Test Scenario's

Update and checkout complete order

"""


@allure.title("Add few items to cart and verify the total count and price is displayed correctly")
@scenario('updateandcheckoutcompleteorder.feature', 'Verify user can delete items in cart')
def test_update_and_checkout_complete_order_1():
    pass


@then(parsers.parse("Add Few Items to Cart {how_many} {items_to_return}"), target_fixture="product_info")
def add_few_items_to_cart(how_many, items_to_return):
    return pytest.shop_steps.react_add_few_items_in_cart(how_many=int(how_many),
                                                         return_items_with_price=bool(items_to_return),
                                                         free_shipping=True, same_item=False)


@then(parsers.parse("Verify total items in cart {cart_value}"))
def verify_total_items_in_cart(cart_value):
    pytest.shop_steps.react_verify_total_items_in_cart(expected_result=str(cart_value))


@then("Click on Shopping cart")
def click_on_shopping_cart():
    pytest.shop_steps.react_open_cart()


@then(parsers.parse("Verify items and prices in cart {status}"))
def verify_items_and_prices_in_cart(product_info, status):
    pytest.shop_steps.react_verify_price_of_items_in_cart(item_info=product_info,
                                                          expected_result=bool(status))


@then(parsers.parse("Remove product items from cart {delete_count}"))
def remove_product_items_from_cart(delete_count):
    pytest.shop_steps.react_remove_items_from_cart(count=int(delete_count))


@then(parsers.parse("Products are not available in cart {status}"))
def products_are_not_available_in_cart(status):
    pytest.shop_steps.react_verify_no_products_in_cart(expected_result=bool(status))


@then(parsers.parse("Sub total value in the cart {value}"), target_fixture="total_price")
def sub_total_value_in_the_cart(value):
    actual_value = pytest.shop_steps.react_sub_total_value_from_in_cart()
    if str(value) == 'None':
        return actual_value
    elif actual_value != str(value):
        try:
            raise AssertionError(f"Cart value is not matching with your value ==> {value}")
        finally:
            quit_browser()


@scenario('updateandcheckoutcompleteorder.feature', 'Verify user is able to place order')
def test_update_and_checkout_cart_test_2():
    pass


@then("Click on checkout in cart")
def click_on_checkout_in_cart():
    pytest.shop_steps.react_click_on_checkout_in_cart()


@then("Get Text from checkout alert message and verify sub total value is equal")
def get_text_from_checkout_alert_message_verify_sub_total_is_equal(total_price):
    actual_price = pytest.shop_steps.react_get_text_from_checkout_alert_message()
    if actual_price != str(total_price):
        try:
            raise AssertionError("Price is not matching from alert text")
        finally:
            quit_browser()


@then("Accept checkout alert message")
def accept_checkout_alert_message():
    pytest.shop_steps.react_accept_checkout_alert_message()


@then("Refresh Shopping page")
def refresh_shopping_page():
    pytest.shop_steps.react_refresh_shopping_page()


"""
Test Scenario's

Add items to cart

"""


@scenario('additemstocart.feature', 'Verify user is able to add same items as desired')
def test_add_items_to_cart_test_2():
    pass


@then(parsers.parse("Add Same item multiple times to cart from dashboard {how_many}"), target_fixture="product_info")
def same_item_add_multiple_items_to_cart_from_dashboard(how_many):
    return pytest.shop_steps.react_add_few_items_in_cart(how_many=int(how_many), same_item=True,
                                                         return_items_with_price=True, free_shipping=True)


@then(parsers.parse("Compare sub total value and items value {how_many}"))
def compare_sub_total_value_and_items_values(product_info, how_many, total_price):
    pytest.shop_steps.react_compare_sub_total_value_and_items_values(actual=product_info, how_many_times=int(how_many),
                                                                     expected_result=total_price)


@then(parsers.parse("Increase items in the cart {how_many_items}"))
def increase_items_in_cart(how_many_items):
    pytest.shop_steps.react_increase_items_in_cart(how_times=int(how_many_items))


@then(parsers.parse("Verify quantity of items in cart {quantity}"))
def verify_quantity_of_items_in_cart(product_info, quantity):
    pytest.shop_steps.react_verify_quantity_of_items_in_cart(item_info=product_info, quantity=quantity)


@scenario('additemstocart.feature', 'Verify items are listed in cart in the order as added to cart with price')
def test_add_items_to_cart_test_1():
    pass


@then(parsers.parse("Add Few items to cart with shipping label {how_many} {items_to_return}"),
      target_fixture="items_with_free")
def add_few_items_in_cart_with_shipping_label(how_many, items_to_return):
    return pytest.shop_steps.react_add_few_items_in_cart_with_shipping_label(how_many=how_many,
                                                                             return_items_with_price=bool(
                                                                                 items_to_return))


@then(parsers.parse("Add Few items to cart without shipping label {how_many} {items_to_return}"),
      target_fixture="items_without_free")
def add_few_items_in_cart_without_shipping_label(how_many, items_to_return):
    return pytest.shop_steps.react_add_few_items_in_cart_without_shipping_label(how_many=how_many,
                                                                                return_items_with_price=bool(
                                                                                    items_to_return))


@then(parsers.parse("Items to check in cart with free & without free shipping {status}"))
def items_to_check_in_cart_with_free_without_free_shipping(status, items_with_free, items_without_free):
    all_cart_items = items_with_free + items_without_free
    pytest.shop_steps.react_verify_price_of_items_in_cart(item_info=all_cart_items,
                                                          expected_result=bool(status))
