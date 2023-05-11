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

from ..models.cooldown import Cooldown
from ..models.scanned_ship import ScannedShip
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateShipShipScanResponse201Data")


class CreateShipShipScanResponse201Data(BaseModel):
    """
    Attributes:
        cooldown (Cooldown): A cooldown is a period of time in which a ship cannot perform certain actions.
        ships (List['ScannedShip']):
    """

    cooldown: "Cooldown" = Field(alias="cooldown")
    ships: List["ScannedShip"] = Field(alias="ships")
    additional_properties: Dict[str, Any] = {}

    class Config:
        arbitrary_types_allowed = True
        allow_population_by_field_name = True

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
