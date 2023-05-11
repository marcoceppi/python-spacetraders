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
from pydantic import BaseModel, Field

from ..models.ship_fuel import ShipFuel
from ..models.ship_nav import ShipNav
from ..types import UNSET, Unset

T = TypeVar("T", bound="WarpShipResponse200Data")


class WarpShipResponse200Data(BaseModel):
    """
    Attributes:
        fuel (ShipFuel): Details of the ship's fuel tanks including how much fuel was consumed during the last transit
            or action.
        nav (ShipNav): The navigation information of the ship.
    """

    fuel: "ShipFuel" = Field(alias="fuel")
    nav: "ShipNav" = Field(alias="nav")
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
