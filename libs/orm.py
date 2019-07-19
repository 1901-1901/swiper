

class ModelToDictMixin():
    def to_dict(self,exclude=[]):
        attr_dict = {}
        fields = self._meta.fields

        for field in fields:
            field_name = fields.attname
            if field_name not in exclude:
                attr_dict[field_name] = getattr(self,field_name)

        return attr_dict