import typing as ty

from pydantic import HttpUrl
from pydantic import BaseModel
from pydantic import field_validator


class House(BaseModel):
    url: ty.Optional[HttpUrl]
    price: ty.Optional[int]
    currency: ty.Optional[ty.Literal["AZN", "USD", "EUR"]]
    location: ty.Optional[str]
    number_of_rooms: ty.Optional[int]
    area: ty.Optional[int]
    floor: ty.Optional[str]
    city: ty.Optional[str]
    announced_date: ty.Optional[str]

    @field_validator("number_of_rooms", "area")
    def validate_fields(cls, v, _values, **kwargs):
        if v is not None and v < 0:
            raise ValueError("Value cannot be less than 0")

        return v
