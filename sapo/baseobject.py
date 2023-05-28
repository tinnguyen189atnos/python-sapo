class SapoObject:
    def __init__(self, **kwargs):
        self.nested_objects = {}
        pass

    @classmethod
    def get(cls, api, id, params={}):
        pass

    @classmethod
    def list(cls, api, params={}):
        pass

    def load(self, data={}):
        for key, value in data.items():
            if key in self.nested_objects.keys():
                setattr(self, key, self.nested_objects[key](value))
                continue
            setattr(self, key, value)
        return self

    def serialize(self):
        data = {}
        for key, value in self.__dict__.items():
            if key in self.get_excluded_attrs():
                continue
            if key in self.nested_objects.keys():
                if isinstance(value, list):
                    data[key] = [v.serialize() for v in value]
                    continue
                data[key] = value.serialize()
                continue
            data[key] = value
        return data

    def get_excluded_attrs(self):
        return ["nested_objects"]

    def __str__(self):
        return "<%s>" % self.__class__.__name__

    def __unicode__(self):
        return "%s" % self.__str__()

    def __repr__(self):
        return str(self)
