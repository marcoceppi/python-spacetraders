import datetime
from typing import (
    TYPE_CHECKING,
    Any,
    BinaryIO,
    Dict,
    List,
    Optional,
    TextIO,
    Tuple,
    Type,
    TypeVar,
    cast,
)

import attr
from dateutil.parser import isoparse
from pydantic import BaseModel, Field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Cooldown")


class Cooldown(BaseModel):
    """A cooldown is a period of time in which a ship cannot perform certain actions.

    Attributes:
        ship_symbol (str): The symbol of the ship that is on cooldown
        total_seconds (int): The total duration of the cooldown in seconds
        remaining_seconds (int): The remaining duration of the cooldown in seconds
        expiration (datetime.datetime): The date and time when the cooldown expires in ISO 8601 format
    """

    ship_symbol: str = Field(alias="shipSymbol")
    total_seconds: int = Field(alias="totalSeconds")
    remaining_seconds: int = Field(alias="remainingSeconds")
    expiration: datetime.datetime = Field(alias="expiration")
    additional_properties: Dict[str, Any] = {}

    class Config:
        arbitrary_types_allowed = True

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
