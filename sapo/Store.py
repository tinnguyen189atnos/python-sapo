from .baseobject import SapoObject


class Store(SapoObject):
    def __init__(self, *args, **kwargs):
        self.id = None
        self.address_1 = None
        self.city = None
        self.country = None
        self.country_code = None
        self.country_name = None
        self.created_on = None
        self.modified_on = None
        self.customer_email = None
        self.currency = None
        self.domain = None
        self.email = None
        self.money_format = None
        self.money_with_currency_format = None
        self.bizweb_domain = None
        self.name = None
        self.plan_name = None
        self.plan_display_name = None
        self.phone = None
        self.province = None
        self.province_code = None
        self.store_owner = None
        self.source = None
        self.timezone = None
        self.has_storefront = None

        super(Store, self).__init__(*args, **kwargs)

    @classmethod
    def get(cls, api):
        store = cls()
        data = api.get("admin/store.json")
        store.load(data.get("store", {}))
        return store
