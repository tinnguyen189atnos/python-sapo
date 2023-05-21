from .baseobject import SapoObject
from .ProductVariant import ProductVariant


class Product(SapoObject):
    def __init__(self, *args, **kwargs):
        self.id = None
        self.name = None
        self.content = None
        self.summary = None
        self.created_on = None
        self.alias = None
        self.images = None
        self.options = None
        self.product_type = None
        self.published_on = None
        self.tags = None
        self.template_layout = None
        self.modified_on = None
        self.variants = None
        self.vendor = None
        self.metafields = None
        self.meta_title = None
        self.meta_description = None
        self.status = None
        self.image = None

        super(Product, self).__init__(*args, **kwargs)
        self.nested_objects = {
            "variants": lambda value: [
                ProductVariant().load(variant) for variant in value
            ]
            if value
            else None,
        }

    @classmethod
    def get(cls, api, id, params={}):
        data = api.get("admin/products/{}.json".format(id), params=params)
        product = cls()
        product.load(data.get("product", {}))
        return product

    @classmethod
    def list(cls, api, params={}):
        total_products = api.get("admin/products/count.json", params=params)
        limit = params.get("limit", 50)
        params["limit"] = limit
        total_pages = total_products.get("count", 0) // limit + 1
        products = []
        for page in range(1, total_pages + 1):
            params["page"] = page
            data = api.get("admin/products.json", params=params)
            for product in data["products"]:
                product_obj = cls()
                product_obj.load(product)
                products.append(product_obj)

        return products
