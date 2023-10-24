import os
import pdb
from decimal import Decimal
from time import sleep
from typing import Union, List
import re
import random
from selenium.webdriver.common.action_chains import ActionChains
from features.utilities.custom_logger import CustomLogger

log = CustomLogger()

# global variables
data_from_text, product_name, element = None, None, None


class ShoppingBase:
    def __init__(self, driver, page_definition):
        self.driver = driver
        self.action = ActionChains(self.driver)
        self.sizes: dict = page_definition['Sizes']
        self.product_tiles: dict = page_definition['ProductsTiles']
        self.products_result: dict = page_definition['ProductsResult']
        self.free_shipping_label: dict = page_definition['FreeShippingLabel']
        self.add_to_cart_button: dict = page_definition['AddToCartButton']
        self.cart: dict = page_definition['Cart']
        self.no_products_in_cart: dict = page_definition['NoProductsInCart']
        self.sub_total: dict = page_definition['SubTotal']
        self.remove_products_from_cart: dict = page_definition['RemoveProductsFromCart']
        self.add_items_in_cart: dict = page_definition['AddItemsInCart']
        self.remove_items_in_cart: dict = page_definition['RemoveItemsInCart']
        self.product_information: dict = page_definition['ProductInformation']
        self.close_cart_popup: dict = page_definition['CloseCartPopup']
        self.total_items_in_cart: dict = page_definition['TotalItemsInCart']
        self.item_price_in_cart: dict = page_definition['ItemPricesInCart']
        self.check_out: dict = page_definition['Checkout']
        self.free_shipping_items = page_definition['FreeShippingItems']
        self.quantity_of_product_in_cart = page_definition['QuantityOfProductInCart']

    def open_shopping_website_in_browser(self) -> None:
        log.debug("Open shopping website in browser")
        self.driver.launch_url_in_browser(url=f"{os.getenv('ShoppingUrl')}")
        self.driver.maximize_browser()

    def apply_which_any_size_filter(self, size_filter: str) -> None:
        log.debug(f"Apply size filter with these size ==> {size_filter}")
        element_value: dict = self.sizes.copy()
        element_value['value'] = element_value['value'].replace("{0}", size_filter)
        log.debug(f"Updated the dict ==> {element_value}")
        self.driver.click_element(element_value)

    def shopping_page_is_loaded(self) -> bool:
        log.debug("Wait till shopping page is loaded")
        return self.driver.element_is_visible(self.product_tiles)

    def fetch_product_results_found(self) -> Union[str, None]:
        log.debug("Fetching products results found from text")
        value = self.driver.get_text_from_value(self.products_result)
        try:
            return str(re.search("(^\d)", value).group(1))
        except AttributeError:
            return None

    def quit_shopping(self) -> None:
        log.debug("Quit shopping..")
        self.driver.quit_browser()

    def fetch_product_title(self) -> List:
        log.debug("Fetch product title method..")
        if isinstance(product := self.driver.wait_and_get_element_list(self.product_information),
                      type(None)) is not None:
            log.info(f'Fetch the product title {[each_element.get_attribute("alt") for each_element in product]}')
            return [each_element.get_attribute("alt") for each_element in product]

    def add_few_items_in_cart(self, count, return_items_with_price=False, free_shipping=False, same_item=False):
        log.debug("Add few items in cart..")
        global data_from_text, product_name, element
        product_info: list = []
        if isinstance(free_shipping_item := self.driver.wait_and_get_element_list(self.product_tiles),
                      type(None)) is not None:
            random.shuffle(free_shipping_item)
            free_shipping_item = ShoppingBase.items_having_free_shipping_tag(items=free_shipping_item,
                                                                             free_shipping=free_shipping)
            if same_item:
                one_item = free_shipping_item[0]
                free_shipping_item.clear()
                for _ in range(0, count):
                    free_shipping_item.append(one_item)
            for start, item in enumerate(free_shipping_item):
                if str(start) == str(count):
                    break
                else:
                    data_from_text = str(item.text).split("\n")
                    if free_shipping:
                        product_name = data_from_text[1]
                        element = self.free_shipping_items.copy()
                    else:
                        product_name = data_from_text[0]
                        element = self.add_to_cart_button.copy()
                    element['value'] = element['value'].replace("{0}", product_name)
                    self.driver.click_element(element)
                    self.driver.click_element(self.close_cart_popup)
                    if return_items_with_price is True:
                        if free_shipping:
                            product_info.append([product_name, data_from_text[2].replace("$", "")])
                        else:
                            product_info.append([product_name, data_from_text[1].replace("$", "")])
        log.debug(f"Items information ==> {product_info}")
        return product_info

    def verify_price_of_items_in_cart(self, item_info):
        status = []
        log.debug("verify price of items in cart..")
        for single_tray in range(0, len(item_info)):
            for item_value in range(0, 1):
                element_update = self.item_price_in_cart.copy()
                element_update['value'] = element_update['value'].replace('{0}', item_info[single_tray][item_value])
                element_update['value'] = element_update['value'].replace('{1}', item_info[single_tray][item_value + 1])
                status.append(self.driver.element_is_visible(element_update))
            return all(status)

    @staticmethod
    def fetch_price_of_the_product_from_dashboard(text):
        log.debug("Fetch price of the product from dashboard..")
        try:
            return "$  " + re.search("([^$]\d+.\d+)", text).group(1)
        except AttributeError:
            return False

    def count_total_items_in_cart(self):
        log.info(
            f"Verify total items in cart {(count_total_items_in_cart := self.driver.get_text_from_value(self.cart))}")
        return count_total_items_in_cart

    def open_cart(self):
        log.debug("Open cart..")
        self.driver.click_element(self.cart)

    def click_on_checkout_in_cart(self):
        log.debug("Click on checkout in cart..")
        self.driver.find_element_by_xpath(self.check_out['value']).click()

    def get_sub_total_value_from_cart(self):
        log.debug(f"Sub total value in cart is {(sub_total_value := self.driver.get_text_from_value(self.sub_total))}")
        return ''.join(sub_total_value.split())

    def accept_checkout_alert_message(self):
        log.debug("Accept checkout alert message..")
        self.driver.accept_alert()

    def get_text_from_checkout_alert_message(self):
        log.info(f"Text from checkout alert message is {(alert_value := self.driver.return_text_from_alert())}")
        log.info(f"After removing the un-necessary characters from alert message, "
                 f"actual value is {(sub_total_actual_value := ShoppingBase.fetch_price_of_the_product_from_dashboard(text=alert_value))}")
        return ''.join(sub_total_actual_value.split())

    def refresh_shopping_page(self):
        log.debug("Refresh shopping page..")
        self.driver.do_page_refresh()

    def verify_no_products_in_cart(self):
        log.debug("verify no products in cart..")
        return self.driver.element_is_visible(self.no_products_in_cart)

    def delete_items_from_the_cart(self, count):
        log.debug("delete items from the cart..")
        for _ in range(0, count):
            self.driver.click_element(self.remove_products_from_cart)

    def increase_items_in_cart(self, how_many):
        log.debug("increase items in cart..")
        for _ in range(0, how_many):
            self.driver.click_element(self.add_items_in_cart)

    @staticmethod
    def compare_sub_total_value_and_items_values(actual, how_many_times):
        log.debug("compare sub total value and items values")
        if actual[1][1].startswith('$'):
            actual[1][1] = actual[1][1].replace('$', '')
        value = Decimal(actual[1][1])
        actual[1][1] = "$" + str(value * how_many_times)
        return actual

    def verify_quantity_of_items_in_cart(self, item_info, quantity):
        log.debug("verify quantity of items in cart..")
        element_update = self.quantity_of_product_in_cart.copy()
        element_update['value'] = element_update['value'].replace('{0}', item_info[0][0])
        element_update['value'] = element_update['value'].replace('{1}', quantity)
        return self.driver.element_is_visible(element_update)

    @staticmethod
    def items_having_free_shipping_tag(items, free_shipping):
        log.debug("items having free shipping tag..")
        items_to_deliver = []
        for each_item in items:
            data_from_text_item = str(each_item.text).split("\n")
            if len(data_from_text_item) == 5 and free_shipping:
                items_to_deliver.append(each_item)
            elif free_shipping is False and len(data_from_text_item) != 5:
                items_to_deliver.append(each_item)
        return items_to_deliver
