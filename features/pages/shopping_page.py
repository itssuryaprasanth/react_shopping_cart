from features.base.shopping_base import ShoppingBase
from features.helpers.json_helper import ObjFromJson


class ShoppingDashBoardPage(ShoppingBase):
    def __init__(self, driver):
        self.json_obj = ObjFromJson()
        page_definition: dict = {
            "Sizes": self.json_obj.get_selected_locator(value="Sizes"),
            "ProductsResult": self.json_obj.get_selected_locator(value="ProductsResult"),
            "ProductsTiles": self.json_obj.get_selected_locator(value="ProductTiles"),
            "FreeShippingLabel": self.json_obj.get_selected_locator(value="FreeShippingLabel"),
            "AddToCartButton": self.json_obj.get_selected_locator(value="AddToCartButton"),
            "Cart": self.json_obj.get_selected_locator(value="Cart"),
            "NoProductsInCart": self.json_obj.get_selected_locator(value="NoProductsInCart"),
            "SubTotal": self.json_obj.get_selected_locator(value="SubTotal"),
            "RemoveProductsFromCart": self.json_obj.get_selected_locator(value="RemoveProductsFromCart"),
            "AddItemsInCart": self.json_obj.get_selected_locator(value="AddItemsInCart"),
            "RemoveItemsInCart": self.json_obj.get_selected_locator(value="RemoveItemsInCart"),
            "ProductInformation": self.json_obj.get_selected_locator(value="ProductInformation"),
            "CloseCartPopup": self.json_obj.get_selected_locator(value="CloseCartPopup"),
            "TotalItemsInCart": self.json_obj.get_selected_locator(value="TotalItemsInCart"),
            "ItemPricesInCart": self.json_obj.get_selected_locator(value="ItemPricesInCart"),
            "Checkout": self.json_obj.get_selected_locator(value="Checkout"),
            "FreeShippingItems": self.json_obj.get_selected_locator(value="FreeShippingItems"),
            "QuantityOfProductInCart": self.json_obj.get_selected_locator(value="QuantityOfProductInCart")
        }
        super().__init__(driver, page_definition)
