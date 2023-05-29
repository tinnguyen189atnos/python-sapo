from sapo.Auth import Auth
from sapo.baseapi import BaseAPI
from sapo.Collect import Collect
from sapo.CustomCollection import CustomCollection
from sapo.Customer import Customer
from sapo.Image import Image
from sapo.Order import Order
from sapo.PriceRule import PriceRule
from sapo.Product import Product
from sapo.ProductVariant import ProductVariant
from sapo.Store import Store


class Client:
    def __init__(self, token, base_url, **kwargs):
        self._api = BaseAPI(token=token, base_url=base_url)

    def get_access_token(self, code, client_id, client_secret):
        return Auth.get_access_token(
            self.api,
            code=code,
            client_id=client_id,
            client_secret=client_secret,
        )

    def get_store(self):
        return Store.get(self.api)

    def get_customer(self, id, params={}):
        return Customer.get(self.api, id, params=params)

    def get_all_customers(self, params={}):
        return Customer.list(self.api, params=params)

    def get_order(self, id, params={}):
        return Order.get(self.api, id, params=params)

    def get_all_orders(self, params={}):
        return Order.list(self.api, params=params)

    def create_product(self, params={}):
        return Product.create(self.api, params=params)

    def update_product(self, id, params={}):
        return Product.update(self.api, id, params=params)

    def get_product(self, id, params={}):
        return Product.get(self.api, id, params=params)

    def get_all_products(self, params={}):
        return Product.list(self.api, params=params)

    def create_custom_collection(self, params={}):
        return CustomCollection.create(self.api, params=params)

    def get_custom_collection(self, id, params={}):
        return CustomCollection.get(self.api, id, params=params)

    def get_all_custom_collections(self, params={}):
        return CustomCollection.list(self.api, params=params)

    def get_price_rule(self, id, params={}):
        return PriceRule.get(self.api, id, params=params)

    def get_all_price_rules(self, params={}):
        return PriceRule.list(self.api, params=params)

    def get_collect(self, id, params={}):
        return Collect.get(self.api, id, params=params)

    def create_collect(self, params={}):
        return Collect.create(self.api, params=params)

    def get_all_collects(self, params={}):
        return Collect.list(self.api, params=params)

    def delete_collect(self, id):
        return Collect.delete(self.api, id)

    def update_product_variant(self, id, params={}):
        return ProductVariant.update(self.api, id, params=params)

    def create_image(self, product_id, params={}):
        return Image.create(self.api, product_id, params=params)

    @property
    def api(self):
        return self._api
