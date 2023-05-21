from .Address import Address
from .baseobject import SapoObject
from .Customer import Customer
from .LineItem import LineItem


class Order(SapoObject):
    def __init__(self, *args, **kwargs):
        self.billing_address = None
        self.browser_ip = None
        self.buyer_accepts_marketing = None
        self.cancel_reason = None
        self.cancelled_on = None
        self.cart_token = None
        self.client_details = None
        self.closed_on = None
        self.created_on = None
        self.currency = None
        self.customer = None
        self.discount_codes = None
        self.email = None
        self.financial_status = None
        self.status = None
        self.fulfillments = None
        self.fulfillment_status = None
        self.tags = None
        self.id = None
        self.landing_site = None
        self.line_items = None
        self.name = None
        self.note = None
        self.note_attributes = None
        self.number = None
        self.order_number = None
        self.payment_gateway_names = None
        self.processed_on = None
        self.processing_method = None
        self.referring_site = None
        self.refunds = None
        self.shipping_address = None
        self.shipping_lines = None
        self.source_name = None
        self.subtotal_price = None
        self.order_token = None
        self.total_discounts = None
        self.total_line_items_price = None
        self.total_price = None
        self.total_weight = None
        self.modified_on = None

        super(Order, self).__init__(*args, **kwargs)
        self.nested_objects = {
            "billing_address": lambda value: Address().load(value) if value else None,
            "customer": lambda value: Customer().load(value) if value else None,
            "line_items": lambda value: [LineItem().load(item) for item in value]
            if value
            else None,
            "shipping_address": lambda value: Address().load(value) if value else None,
        }

    @classmethod
    def get(cls, api, id, params={}):
        data = api.get("admin/orders/{}.json".format(id), params=params)
        order = cls()
        order.load(data.get("order", {}))
        return order

    @classmethod
    def list(cls, api, params={}):
        total_orders = api.get("admin/orders/count.json", params=params)
        limit = params.get("limit", 50)
        params["limit"] = limit
        total_pages = total_orders.get("count", 0) // limit + 1
        orders = []
        for page in range(1, total_pages + 1):
            params["page"] = page
            data = api.get("admin/orders.json", params=params)
            for order in data["orders"]:
                order_obj = cls()
                order_obj.load(order)
                orders.append(order_obj)

        return orders
