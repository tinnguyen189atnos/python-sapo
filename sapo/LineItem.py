from .baseobject import SapoObject


class LineItem(SapoObject):
    def __init__(self, *args, **kwargs):
        self.id = None
        self.fulfillable_quantity = None
        self.fulfillment_service = None
        self.fulfillment_status = None
        self.grams = None
        self.price = None
        self.product_id = None
        self.quantity = None
        self.requires_shipping = None
        self.sku = None
        self.title = None
        self.variant_id = None
        self.variant_title = None
        self.vendor = None
        self.name = None
        self.gift_card = None
        self.taxable = None
        self.tax_lines = None
        self.total_discount = None

        super(LineItem, self).__init__(*args, **kwargs)
