import pydantic as pd


class AllOptional(pd.main.ModelMetaclass):
    """
    Metaclass that makes all fields optional.
    Ref: https://stackoverflow.com/questions/67699451/make-every-field-as-optional-with-pydantic
    """

    def __new__(cls, name, bases, namespaces, **kwargs):
        annotations = namespaces.get("__annotations__", {})
        for base in bases:
            annotations.update(base.__annotations__)
        for field in annotations:
            if not field.startswith("__"):
                annotations[field] = Optional[annotations[field]]
        namespaces["__annotations__"] = annotations
        return super().__new__(cls, name, bases, namespaces, **kwargs)
