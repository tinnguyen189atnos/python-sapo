from .baseobject import SapoObject


class PriceRule(SapoObject):
    def __init__(self, *args, **kwargs):
        self.id = None
        self.created_on = None
        self.title = None
        self.target_type = None
        self.target_selection = None
        self.allocation_method = None
        self.value_type = None
        self.value = None
        self.exclude_type = None
        self.once_per_customer = None
        self.usage_limit = None
        self.customer_selection = None
        self.prerequisite_saved_search_ids = None
        self.prerequisite_subtotal_range = None
        self.prerequisite_quantity_range = None
        self.prerequisite_shipping_price_range = None
        self.entitled_product_ids = None
        self.entitled_collection_ids = None
        self.entitled_country_ids = None
        self.starts_on = None
        self.ends_on = None

        super(PriceRule, self).__init__(*args, **kwargs)

    @classmethod
    def get(cls, api, params={}):
        price_rule = cls()
        data = api.get("admin/price_rules.json", params=params)
        price_rule.load(data.get("price_rules", {}))
        return price_rule

    @classmethod
    def list(cls, api, params={}):
        total_price_rules = api.get("admin/price_rules/count.json", params=params)
        limit = params.get("limit", 50)
        params["limit"] = limit
        total_pages = total_price_rules.get("count", 0) // limit + 1
        price_rules = []
        for page in range(1, total_pages + 1):
            params["page"] = page
            data = api.get("admin/price_rules.json", params=params)
            for price_rule in data["price_rules"]:
                price_rule_obj = cls()
                price_rule_obj.load(price_rule)
                price_rules.append(price_rule_obj)

        return price_rules
