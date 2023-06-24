from typing import (
    Any,
    Dict,
    List,
    TypeVar,
    Union,
)

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
            symbol (ShipFrameSymbol): Symbol of the frame.
            name (str): Name of the frame.
            description (str): Description of the frame.
            module_slots (int): The amount of slots that can be dedicated to modules installed in the ship. Each installed
                module take up a number of slots, and once there are no more slots, no new modules can be installed.
            mounting_points (int): The amount of slots that can be dedicated to mounts installed in the ship. Each installed
                mount takes up a number of points, and once there are no more points remaining, no new mounts can be installed.
            fuel_capacity (int): The maximum amount of fuel that can be stored in this ship. When refueling, the ship will
                be refueled to this amount.
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
    condition: Union[Unset, int] = Field(UNSET, alias="condition")
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
