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

    def __str__(self):
        return "<%s>" % self.__class__.__name__

    def __unicode__(self):
        return "%s" % self.__str__()

    def __repr__(self):
        return str(self)
