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

from ..models.system_type import SystemType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ScannedSystem")


@attr.s(auto_attribs=True)
class ScannedSystem:
    """
    Attributes:
        symbol (str):
        sector_symbol (str):
        type (SystemType): The type of waypoint.
        x (int):
        y (int):
        distance (int):
    """

    symbol: str
    sector_symbol: str
    type: SystemType
    x: int
    y: int
    distance: int
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        symbol = self.symbol
        sector_symbol = self.sector_symbol
        type = self.type.value

        x = self.x
        y = self.y
        distance = self.distance

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "symbol": symbol,
                "sectorSymbol": sector_symbol,
                "type": type,
                "x": x,
                "y": y,
                "distance": distance,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        symbol = d.pop("symbol")

        sector_symbol = d.pop("sectorSymbol")

        type = SystemType(d.pop("type"))

        x = d.pop("x")

        y = d.pop("y")

        distance = d.pop("distance")

        scanned_system = cls(
            symbol=symbol,
            sector_symbol=sector_symbol,
            type=type,
            x=x,
            y=y,
            distance=distance,
        )

        scanned_system.additional_properties = d
        return scanned_system

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
