from typing import (
    Any,
    Dict,
    List,
    TypeVar,
    Union,
)

from pydantic import BaseModel, Field

from ..models.ship_fuel_consumed import ShipFuelConsumed
from ..types import UNSET, Unset

T = TypeVar("T", bound="ShipFuel")


class ShipFuel(BaseModel):
    """Details of the ship's fuel tanks including how much fuel was consumed during the last transit or action.

    Attributes:
        current (int): The current amount of fuel in the ship's tanks.
        capacity (int): The maximum amount of fuel the ship's tanks can hold.
        consumed (Union[Unset, ShipFuelConsumed]): An object that only shows up when an action has consumed fuel in the
            process. Shows the fuel consumption data.
    """

    current: int = Field(alias="current")
    capacity: int = Field(alias="capacity")
    consumed: Union[Unset, "ShipFuelConsumed"] = Field(UNSET, alias="consumed")
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
