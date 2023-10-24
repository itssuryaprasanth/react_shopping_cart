from features.pages.shopping_page import ShoppingDashBoardPage
from features.fixtures.set_environment import create_environment
from features.utilities.custom_logger import CustomLogger
import allure
from time import sleep

log = CustomLogger()


class ShoppingSteps:
    def __init__(self):
        self.shopping_steps = ShoppingDashBoardPage(driver=create_environment().get_driver())
        self.product_title_information = []

    @allure.step("Open Shopping website")
    def react_open_shopping_website_in_browser(self):
        self.shopping_steps.open_shopping_website_in_browser()

    @allure.step("Apply any size filter")
    def react_apply_which_any_size_filter(self, size):
        self.shopping_steps.apply_which_any_size_filter(size_filter=size)

    @allure.step("Shopping page is loaded")
    def react_shopping_page_is_loaded(self, expected_result=True):
        actual_result = self.shopping_steps.shopping_page_is_loaded()
        assert actual_result == expected_result, 'Shopping page is not loaded'

    @allure.step("Fetch product results found")
    def react_fetch_product_results_found(self, expected_result):
        if isinstance(product_results := self.shopping_steps.fetch_product_results_found(), type(None)):
            return False
        elif expected_result != product_results:
            return False
        else:
            log.info("Correct product results are displayed..")
            return True

    @allure.step("Quit shopping")
    def react_quit_shopping(self):
        self.shopping_steps.quit_shopping()

    @allure.step("Fetch Product title")
    def react_fetch_product_title(self):
        for product_title in self.shopping_steps.fetch_product_title():
            self.product_title_information.append(product_title)
        log.debug(f"The product information is ==> {self.product_title_information}")

    @allure.step("Verify product titles after applying multiple filters")
    def react_verify_product_titles_after_applying_multiple_filters(self):
        product_titles = self.product_title_information
        self.product_title_information.clear()
        self.react_fetch_product_title()
        if product_titles != self.product_title_information:
            assert "Product Titles are not matching..."
        else:
            log.info("Product Titles are matching...")

    @allure.step("Add few items into the cart")
    def react_add_few_items_in_cart(self, how_many, return_items_with_price, free_shipping, same_item):
        return self.shopping_steps.add_few_items_in_cart(return_items_with_price=return_items_with_price,
                                                         count=how_many, free_shipping=free_shipping,
                                                         same_item=same_item)

    @allure.step("Add few items into the cart having free shipping label")
    def react_add_few_items_in_cart_with_shipping_label(self, how_many, return_items_with_price):
        return self.shopping_steps.add_few_items_in_cart(return_items_with_price=return_items_with_price,
                                                         free_shipping=True, count=how_many, same_item=False)

    @allure.step("Add few items into the cart not having free shipping label")
    def react_add_few_items_in_cart_without_shipping_label(self, how_many, return_items_with_price):
        return self.shopping_steps.add_few_items_in_cart(return_items_with_price=return_items_with_price,
                                                         free_shipping=False, count=how_many, same_item=False)

    @allure.step("Verify prices of items in the cart page")
    def react_verify_price_of_items_in_cart(self, item_info, expected_result):
        actual_result = self.shopping_steps.verify_price_of_items_in_cart(item_info)
        assert actual_result == expected_result, "Prices are not matching with products | products are not matching " \
                                                 "with prices "

    @allure.step("Verify total items in the cart page")
    def react_verify_total_items_in_cart(self, expected_result):
        log.info(f"Expected result {expected_result}")
        actual_result = self.shopping_steps.count_total_items_in_cart()
        log.info(f"Actual result {actual_result}")
        assert str(actual_result) == str(expected_result), "Total Items in cart are not equal"

    @allure.step("Click on cart")
    def react_open_cart(self):
        self.shopping_steps.open_cart()

    @allure.step("Click on checkout in cart page")
    def react_click_on_checkout_in_cart(self):
        self.shopping_steps.click_on_checkout_in_cart()

    @allure.step("Accept checkout alert message")
    def react_accept_checkout_alert_message(self):
        self.shopping_steps.accept_checkout_alert_message()

    @allure.step("Get text from checkout alert message")
    def react_get_text_from_checkout_alert_message(self):
        return self.shopping_steps.get_text_from_checkout_alert_message()

    @allure.step("Sub total value in the cart")
    def react_sub_total_value_from_in_cart(self):
        return self.shopping_steps.get_sub_total_value_from_cart()

    @allure.step("Refresh shopping page")
    def react_refresh_shopping_page(self):
        self.shopping_steps.refresh_shopping_page()

    @allure.step("Verify no products in cart")
    def react_verify_no_products_in_cart(self, expected_result):
        actual_result = self.shopping_steps.verify_no_products_in_cart()
        assert actual_result == expected_result, "Products are preset in the cart.."

    @allure.step("Remove items in the cart")
    def react_remove_items_from_cart(self, count):
        self.shopping_steps.delete_items_from_the_cart(count)

    @allure.step("Verify sub total cart value is zero")
    def react_verify_sub_total_cart_value_is_zero(self):
        return self.react_sub_total_value_from_in_cart()

    @allure.step("Increase items in the cart")
    def react_increase_items_in_cart(self, how_times):
        self.shopping_steps.increase_items_in_cart(how_times)

    @allure.step("Compare sub total value and items values")
    def react_compare_sub_total_value_and_items_values(self, actual, how_many_times, expected_result):
        self.shopping_steps.compare_sub_total_value_and_items_values(actual=actual, how_many_times=how_many_times)
        assert actual[1][1] == expected_result, "Cart Value is not matching with items values"

    @allure.step("Add same item multiple items to cart from dashboard")
    def react_verify_quantity_of_items_in_cart(self, item_info, quantity):
        self.shopping_steps.verify_quantity_of_items_in_cart(item_info=item_info, quantity=quantity)
