from .baseobject import SapoObject


class ProductVariant(SapoObject):
    def __init__(self, *args, **kwargs):
        self.id = None
        self.barcode = None
        self.compare_at_price = None
        self.created_on = None
        self.grams = None
        self.inventory_management = None
        self.inventory_policy = None
        self.inventory_quantity = None
        self.inventory_quantity_adjustment = None
        self.metafield = None
        self.option = None
        self.position = None
        self.price = None
        self.product_id = None
        self.requires_shipping = None
        self.sku = None
        self.title = None
        self.modified_on = None
        self.weight = None
        self.weight_unit = None
        self.image_id = None

        super(ProductVariant, self).__init__(*args, **kwargs)

    @classmethod
    def create(cls, api, params={}):
        pass

    @classmethod
    def update(cls, api, id, params={}):
        data = api.put("admin/variants/%s.json" % id, params=params)
        variant = cls()
        variant.load(data.get("variant", {}))
        return variant
