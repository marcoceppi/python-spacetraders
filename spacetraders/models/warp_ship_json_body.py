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

T = TypeVar("T", bound="WarpShipJsonBody")


@attr.s(auto_attribs=True)
class WarpShipJsonBody:
    """
    Attributes:
        waypoint_symbol (str): The target destination.
    """

    waypoint_symbol: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        waypoint_symbol = self.waypoint_symbol

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "waypointSymbol": waypoint_symbol,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        waypoint_symbol = d.pop("waypointSymbol")

        warp_ship_json_body = cls(
            waypoint_symbol=waypoint_symbol,
        )

        warp_ship_json_body.additional_properties = d
        return warp_ship_json_body

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
