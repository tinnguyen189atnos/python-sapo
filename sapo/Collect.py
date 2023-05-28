from .baseobject import SapoObject


class Collect(SapoObject):
    def __init__(self, *args, **kwargs):
        self.id = None
        self.collection_id = None
        self.product_id = None
        self.position = None
        self.featured = None
        self.created_on = None
        self.modified_on = None

        super(Collect, self).__init__(*args, **kwargs)

    @classmethod
    def create(cls, api, params={}):
        data = api.post("admin/collects.json", params=params)
        collect = cls()
        collect.load(data.get("collect", {}))
        return collect

    @classmethod
    def get(cls, api, id, params={}):
        data = api.get("admin/collects/{}.json".format(id), params=params)
        collect = cls()
        collect.load(data.get("collect", {}))
        return collect

    @classmethod
    def list(cls, api, params={}):
        total_collects = api.get("admin/collects/count.json", params=params)
        limit = params.get("limit", 50)
        params["limit"] = limit
        total_pages = total_collects.get("count", 0) // limit + 1
        collects = []
        for page in range(1, total_pages + 1):
            params["page"] = page
            data = api.get("admin/collects.json", params=params)
            for collect in data["collects"]:
                collect_obj = cls()
                collect_obj.load(collect)
                collects.append(collect_obj)

        return collects

    @classmethod
    def delete(cls, api, id):
        return api.delete("admin/collects/{}.json".format(id))
