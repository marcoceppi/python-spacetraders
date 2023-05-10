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
    Union,
)

import attr

from ..models.ship_nav_flight_mode import ShipNavFlightMode
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchShipNavJsonBody")


@attr.s(auto_attribs=True)
class PatchShipNavJsonBody:
    """
    Attributes:
        flight_mode (Union[Unset, ShipNavFlightMode]): The ship's set speed when traveling between waypoints or systems.
            Default: ShipNavFlightMode.CRUISE.
    """

    flight_mode: Union[Unset, ShipNavFlightMode] = ShipNavFlightMode.CRUISE
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        flight_mode: Union[Unset, str] = UNSET
        if not isinstance(self.flight_mode, Unset):
            flight_mode = self.flight_mode.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if flight_mode is not UNSET:
            field_dict["flightMode"] = flight_mode

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _flight_mode = d.pop("flightMode", UNSET)
        flight_mode: Union[Unset, ShipNavFlightMode]
        if isinstance(_flight_mode, Unset):
            flight_mode = UNSET
        else:
            flight_mode = ShipNavFlightMode(_flight_mode)

        patch_ship_nav_json_body = cls(
            flight_mode=flight_mode,
        )

        patch_ship_nav_json_body.additional_properties = d
        return patch_ship_nav_json_body

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
