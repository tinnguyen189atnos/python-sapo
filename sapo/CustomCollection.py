from .baseobject import SapoObject


class CustomCollection(SapoObject):
    def __init__(self, *args, **kwargs):
        self.id = None
        self.name = None
        self.alias = None
        self.description = None
        self.published_on = None
        self.meta_title = None
        self.meta_description = None
        self.created_on = None
        self.modified_on = None
        self.template_layout = None
        self.sort_order = None
        self.image = None
        self.products_count = None
        self.rules = None
        self.disjunctive = None

        super(CustomCollection, self).__init__(*args, **kwargs)

    @classmethod
    def create(cls, api, params={}):
        data = api.post("admin/custom_collections.json", params=params)
        custom_collection = cls()
        custom_collection.load(data.get("custom_collection", {}))
        return custom_collection

    @classmethod
    def get(cls, api, id, params={}):
        data = api.get("admin/custom_collections/{}.json".format(id), params=params)
        custom_collection = cls()
        custom_collection.load(data.get("custom_collection", {}))
        return custom_collection

    @classmethod
    def list(cls, api, params={}):
        total_custom_collections = api.get(
            "admin/custom_collections/count.json", params=params
        )
        limit = params.get("limit", 50)
        params["limit"] = limit
        total_pages = total_custom_collections.get("count", 0) // limit + 1
        custom_collections = []
        for page in range(1, total_pages + 1):
            params["page"] = page
            data = api.get("admin/custom_collections.json", params=params)
            for custom_collection in data["custom_collections"]:
                custom_collection_obj = cls()
                custom_collection_obj.load(custom_collection)
                custom_collections.append(custom_collection_obj)

        return custom_collections
