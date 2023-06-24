from typing import (
    Any,
    Dict,
    List,
    TypeVar,
)

from pydantic import BaseModel, Field

from ..models.ship_cargo_item import ShipCargoItem
from ..types import Unset

T = TypeVar("T", bound="ShipCargo")


class ShipCargo(BaseModel):
    """Ship cargo details.

    Attributes:
        capacity (int): The max number of items that can be stored in the cargo hold.
        units (int): The number of items currently stored in the cargo hold.
        inventory (List['ShipCargoItem']): The items currently in the cargo hold.
    """

    capacity: int = Field(alias="capacity")
    units: int = Field(alias="units")
    inventory: List["ShipCargoItem"] = Field(alias="inventory")
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
