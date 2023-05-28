from .baseobject import SapoObject


class Image(SapoObject):
    def __init__(self, *args, **kwargs):
        self.id = None
        self.product_id = None
        self.position = None
        self.created_on = None
        self.modified_on = None
        self.src = None
        self.variant_ids = None
        super(Image, self).__init__(*args, **kwargs)
