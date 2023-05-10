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

from ..types import UNSET, Unset

T = TypeVar("T", bound="Cooldown")


@attr.s(auto_attribs=True)
class Cooldown:
    """A cooldown is a period of time in which a ship cannot perform certain actions.

    Attributes:
        ship_symbol (str): The symbol of the ship that is on cooldown
        total_seconds (int): The total duration of the cooldown in seconds
        remaining_seconds (int): The remaining duration of the cooldown in seconds
        expiration (datetime.datetime): The date and time when the cooldown expires in ISO 8601 format
    """

    ship_symbol: str
    total_seconds: int
    remaining_seconds: int
    expiration: datetime.datetime
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ship_symbol = self.ship_symbol
        total_seconds = self.total_seconds
        remaining_seconds = self.remaining_seconds
        expiration = self.expiration.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "shipSymbol": ship_symbol,
                "totalSeconds": total_seconds,
                "remainingSeconds": remaining_seconds,
                "expiration": expiration,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        ship_symbol = d.pop("shipSymbol")

        total_seconds = d.pop("totalSeconds")

        remaining_seconds = d.pop("remainingSeconds")

        expiration = isoparse(d.pop("expiration"))

        cooldown = cls(
            ship_symbol=ship_symbol,
            total_seconds=total_seconds,
            remaining_seconds=remaining_seconds,
            expiration=expiration,
        )

        cooldown.additional_properties = d
        return cooldown

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
