from .Address import Address
from .baseobject import SapoObject


class Customer(SapoObject):
    def __init__(self, *args, **kwargs):
        self.id = None
        self.accepts_marketing = None
        self.addresses = None
        self.created_on = None
        self.default_address = None
        self.email = None
        self.first_name = None
        self.phone = None
        self.metafield = None
        self.last_name = None
        self.last_order_id = None
        self.last_order_name = None
        self.note = None
        self.orders_count = None
        self.state = None
        self.tags = None
        self.total_spent = None
        self.modified_on = None
        self.verified_email = None
        self.dob = None

        super(Customer, self).__init__(*args, **kwargs)
        self.nested_objects = {
            "default_address": lambda value: Address().load(value) if value else None,
            "addresses": lambda value: [Address().load(address) for address in value]
            if value
            else None,
        }

    @classmethod
    def get(cls, api, id, params={}):
        data = api.get("admin/customers/{}.json".format(id), params=params)
        customer = cls()
        customer.load(data.get("customer", {}))
        return customer

    @classmethod
    def list(cls, api, params={}):
        total_customers = api.get("admin/customers/count.json", params=params)
        limit = params.get("limit", 50)
        params["limit"] = limit
        total_pages = total_customers.get("count", 0) // limit + 1
        customers = []
        for page in range(1, total_pages + 1):
            params["page"] = page
            data = api.get("admin/customers.json", params=params)
            for customer in data["customers"]:
                customer_obj = cls()
                customer_obj.load(customer)
                customers.append(customer_obj)

        return customers
