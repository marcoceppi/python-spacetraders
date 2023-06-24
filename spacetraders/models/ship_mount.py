from typing import (
    Any,
    Dict,
    List,
    TypeVar,
    Union,
)

from pydantic import BaseModel, Field

from ..models.ship_mount_deposits_item import ShipMountDepositsItem
from ..models.ship_mount_symbol import ShipMountSymbol
from ..models.ship_requirements import ShipRequirements
from ..types import UNSET, Unset

T = TypeVar("T", bound="ShipMount")


class ShipMount(BaseModel):
    """A mount is installed on the exterier of a ship.

    Attributes:
        symbol (ShipMountSymbol): Symbo of this mount.
        name (str): Name of this mount.
        requirements (ShipRequirements): The requirements for installation on a ship
        description (Union[Unset, str]): Description of this mount.
        strength (Union[Unset, int]): Mounts that have this value, such as mining lasers, denote how powerful this
            mount's capabilities are.
        deposits (Union[Unset, List[ShipMountDepositsItem]]): Mounts that have this value denote what goods can be
            produced from using the mount.
    """

    symbol: ShipMountSymbol = Field(alias="symbol")
    name: str = Field(alias="name")
    requirements: "ShipRequirements" = Field(alias="requirements")
    description: Union[Unset, str] = Field(UNSET, alias="description")
    strength: Union[Unset, int] = Field(UNSET, alias="strength")
    deposits: Union[Unset, List[ShipMountDepositsItem]] = Field(UNSET, alias="deposits")
    additional_properties: Dict[str, Any] = {}

    class Config:
        arbitrary_types_allowed = True
        allow_population_by_field_name = True

    def dict(self, *args, **kwargs):
        output = super().dict(*args, **kwargs)
        return {k: v for k, v in output.items() if not isinstance(v, Unset)}

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
