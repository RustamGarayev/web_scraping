import typing as ty

from pydantic import HttpUrl
from pydantic import BaseModel
from pydantic import field_validator

from models import AllOptional


class House(BaseModel, metaclass=AllOptional):
    url: HttpUrl
    price: int
    currency: ty.Literal["AZN", "USD", "EUR"]
    location: str
    number_of_rooms: int
    area: int
    floor: str
    city: str
    announced_date: str

    @classmethod
    @field_validator("number_of_rooms", "area")
    def validate_fields(cls, v, _values, **_kwargs):
        if v is not None and v < 0:
            raise ValueError("Value cannot be less than 0")

        return v
