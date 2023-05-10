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
)

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ShipCargoItem")


@attr.s(auto_attribs=True)
class ShipCargoItem:
    """The type of cargo item and the number of units.

    Attributes:
        symbol (str): The unique identifier of the cargo item type.
        name (str): The name of the cargo item type.
        description (str): The description of the cargo item type.
        units (int): The number of units of the cargo item.
    """

    symbol: str
    name: str
    description: str
    units: int
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        symbol = self.symbol
        name = self.name
        description = self.description
        units = self.units

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "symbol": symbol,
                "name": name,
                "description": description,
                "units": units,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        symbol = d.pop("symbol")

        name = d.pop("name")

        description = d.pop("description")

        units = d.pop("units")

        ship_cargo_item = cls(
            symbol=symbol,
            name=name,
            description=description,
            units=units,
        )

        ship_cargo_item.additional_properties = d
        return ship_cargo_item

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
