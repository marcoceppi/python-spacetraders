from typing import (
    Any,
    Dict,
    List,
    TypeVar,
    Union,
)

from pydantic import BaseModel, Field

from ..models.ship_engine_symbol import ShipEngineSymbol
from ..models.ship_requirements import ShipRequirements
from ..types import UNSET, Unset

T = TypeVar("T", bound="ShipEngine")


class ShipEngine(BaseModel):
    """The engine determines how quickly a ship travels between waypoints.

    Attributes:
        symbol (ShipEngineSymbol): The symbol of the engine.
        name (str): The name of the engine.
        description (str): The description of the engine.
        speed (int): The speed stat of this engine. The higher the speed, the faster a ship can travel from one point to
            another. Reduces the time of arrival when navigating the ship.
        requirements (ShipRequirements): The requirements for installation on a ship
        condition (Union[Unset, int]): Condition is a range of 0 to 100 where 0 is completely worn out and 100 is brand
            new.
    """

    symbol: ShipEngineSymbol = Field(alias="symbol")
    name: str = Field(alias="name")
    description: str = Field(alias="description")
    speed: int = Field(alias="speed")
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
