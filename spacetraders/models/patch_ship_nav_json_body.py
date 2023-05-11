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
from pydantic import BaseModel, Field

from ..models.ship_nav_flight_mode import ShipNavFlightMode
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchShipNavJsonBody")


class PatchShipNavJsonBody(BaseModel):
    """
    Attributes:
        flight_mode (Union[Unset, ShipNavFlightMode]): The ship's set speed when traveling between waypoints or systems.
            Default: ShipNavFlightMode.CRUISE.
    """

    flight_mode: Union[Unset, ShipNavFlightMode] = ShipNavFlightMode.CRUISE
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
