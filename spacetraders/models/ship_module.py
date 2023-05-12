from typing import (
    Any,
    Dict,
    List,
    TypeVar,
    Union,
)

from pydantic import BaseModel, Field

from ..models.ship_module_symbol import ShipModuleSymbol
from ..models.ship_requirements import ShipRequirements
from ..types import UNSET, Unset

T = TypeVar("T", bound="ShipModule")


class ShipModule(BaseModel):
    """A module can be installed in a ship and provides a set of capabilities such as storage space or quarters for crew.
    Module installations are permanent.

        Attributes:
            symbol (ShipModuleSymbol):
            name (str):
            requirements (ShipRequirements): The requirements for installation on a ship
            capacity (Union[Unset, int]):
            range_ (Union[Unset, int]):
            description (Union[Unset, str]):
    """

    symbol: ShipModuleSymbol = Field(alias="symbol")
    name: str = Field(alias="name")
    requirements: "ShipRequirements" = Field(alias="requirements")
    capacity: Union[Unset, int] = Field(UNSET, alias="capacity")
    range_: Union[Unset, int] = Field(UNSET, alias="range")
    description: Union[Unset, str] = Field(UNSET, alias="description")
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
