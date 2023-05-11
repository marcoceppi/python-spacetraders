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

from ..models.ship_frame_symbol import ShipFrameSymbol
from ..models.ship_requirements import ShipRequirements
from ..types import UNSET, Unset

T = TypeVar("T", bound="ShipFrame")


class ShipFrame(BaseModel):
    """The frame of the ship. The frame determines the number of modules and mounting points of the ship, as well as base
    fuel capacity. As the condition of the frame takes more wear, the ship will become more sluggish and less
    maneuverable.

        Attributes:
            symbol (ShipFrameSymbol):
            name (str):
            description (str):
            module_slots (int):
            mounting_points (int):
            fuel_capacity (int):
            requirements (ShipRequirements): The requirements for installation on a ship
            condition (Union[Unset, int]): Condition is a range of 0 to 100 where 0 is completely worn out and 100 is brand
                new.
    """

    symbol: ShipFrameSymbol = Field(alias="symbol")
    name: str = Field(alias="name")
    description: str = Field(alias="description")
    module_slots: int = Field(alias="moduleSlots")
    mounting_points: int = Field(alias="mountingPoints")
    fuel_capacity: int = Field(alias="fuelCapacity")
    requirements: "ShipRequirements" = Field(alias="requirements")
    condition: Union[Unset, int] = UNSET
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
