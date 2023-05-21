from .baseobject import SapoObject


class Address(SapoObject):
    def __init__(self, *args, **kwargs):
        self.address1 = None
        self.address2 = None
        self.city = None
        self.company = None
        self.country = None
        self.first_name = None
        self.last_name = None
        self.phone = None
        self.province = None
        self.zip = None
        self.name = None
        self.province_code = None
        self.country_code = None
        self.default = None
        self.email = None
        super(Address, self).__init__(*args, **kwargs)
