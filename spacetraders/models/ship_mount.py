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
    cast,
)

import attr
from pydantic import BaseModel, Field

from ..models.ship_mount_deposits_item import ShipMountDepositsItem
from ..models.ship_mount_symbol import ShipMountSymbol
from ..models.ship_requirements import ShipRequirements
from ..types import UNSET, Unset

T = TypeVar("T", bound="ShipMount")


class ShipMount(BaseModel):
    """A mount is installed on the exterier of a ship.

    Attributes:
        symbol (ShipMountSymbol):
        name (str):
        requirements (ShipRequirements): The requirements for installation on a ship
        description (Union[Unset, str]):
        strength (Union[Unset, int]):
        deposits (Union[Unset, List[ShipMountDepositsItem]]):
    """

    symbol: ShipMountSymbol = Field(alias="symbol")
    name: str = Field(alias="name")
    requirements: "ShipRequirements" = Field(alias="requirements")
    description: Union[Unset, str] = UNSET
    strength: Union[Unset, int] = UNSET
    deposits: Union[Unset, List[ShipMountDepositsItem]] = UNSET
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
