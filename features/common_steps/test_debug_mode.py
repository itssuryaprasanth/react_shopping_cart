from time import sleep

from features.common_steps.common_steps import ShoppingSteps


def test_verify_user_is_able_to_place_order():
    shop_steps = ShoppingSteps()
    shop_steps.react_open_shopping_website_in_browser()
    shop_steps.react_shopping_page_is_loaded()
    shop_steps.react_add_few_items_in_cart(how_many=1, free_shipping=True, return_items_with_price=True)
    shop_steps.react_open_cart()
    price = shop_steps.react_sub_total_value_from_in_cart()
    shop_steps.react_click_on_checkout_in_cart()
    shop_steps.react_get_text_from_checkout_alert_message()
    shop_steps.react_accept_checkout_alert_message()
    shop_steps.react_refresh_shopping_page()
    shop_steps.react_open_cart()
    shop_steps.react_verify_no_products_in_cart(expected_result=True)

# def test_verify_user_can_delete_items_in_cart():
#     # Test 1
#     shop_steps = ShoppingSteps()
#     shop_steps.react_open_shopping_website_in_browser()
#     shop_steps.react_shopping_page_is_loaded()
#     shop_steps.react_add_few_items_in_cart(2)
#     shop_steps.react_verify_total_items_in_cart(2)

# def test_verify_user_can_delete_items_in_cart_test2():
#     shop_steps = ShoppingSteps()
#     shop_steps.react_open_shopping_website_in_browser()
#     shop_steps.react_shopping_page_is_loaded()
#     products_with_price = shop_steps.react_add_few_items_in_cart(2, return_items_with_price=True)
#     shop_steps.react_verify_total_items_in_cart(2)
#     shop_steps.react_open_cart()
#     shop_steps.react_verify_price_of_items_in_cart(item_info=products_with_price, expected_result=True)
#     shop_steps.react_remove_items_from_cart(2)
#     shop_steps.react_verify_no_products_in_cart(expected_result=True)
#     price = shop_steps.react_sub_total_value_from_in_cart()
#     assert price == "$0.00"
# shop_steps.react_add_few_items_in_cart(how_many=4, return_items_with_price=True, free_shipping=True)
# shop_steps.react_add_few_items_in_cart(how_many=1, return_items_with_price=True, free_shipping=False)


def test_verify_items_are_listed_in_cart_in_the_order_as_added_to_cart_with_price():

    shop_steps = ShoppingSteps()
    shop_steps.react_open_shopping_website_in_browser()
    shop_steps.react_shopping_page_is_loaded()
    # test 1 items_information = shop_steps.react_same_item_add_multiple_times_to_cart_from_dashboard(
    # how_many_items=2) shop_steps.react_open_cart() shop_steps.react_verify_price_of_items_in_cart(
    # item_info=items_information, expected_result=True) value = shop_steps.react_sub_total_value_from_in_cart()
    # shop_steps.react_compare_sub_total_value_and_items_values(actual=items_information, how_many_times=2,
    # expected_result=value) test 2 items_information =
    # shop_steps.react_same_item_add_multiple_times_to_cart_from_dashboard(how_many_items=2)
    # shop_steps.react_open_cart() shop_steps.react_increase_items_in_cart(2)
    # shop_steps.react_verify_price_of_items_in_cart(item_info=items_information, expected_result=True) value =
    # shop_steps.react_sub_total_value_from_in_cart() shop_steps.react_compare_sub_total_value_and_items_values(
    # actual=items_information, how_many_times=2, expected_result=value)

    print(shop_steps.react_add_few_items_in_cart(how_many=4, free_shipping=True, return_items_with_price=True))
    print(shop_steps.react_add_few_items_in_cart(how_many=1, free_shipping=False, return_items_with_price=True))








