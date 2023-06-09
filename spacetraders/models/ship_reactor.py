from typing import (
    Any,
    Dict,
    List,
    TypeVar,
    Union,
)

from pydantic import BaseModel, Field

from ..models.ship_reactor_symbol import ShipReactorSymbol
from ..models.ship_requirements import ShipRequirements
from ..types import UNSET, Unset

T = TypeVar("T", bound="ShipReactor")


class ShipReactor(BaseModel):
    """The reactor of the ship. The reactor is responsible for powering the ship's systems and weapons.

    Attributes:
        symbol (ShipReactorSymbol): Symbol of the reactor.
        name (str): Name of the reactor.
        description (str): Description of the reactor.
        power_output (int): The amount of power provided by this reactor. The more power a reactor provides to the ship,
            the lower the cooldown it gets when using a module or mount that taxes the ship's power.
        requirements (ShipRequirements): The requirements for installation on a ship
        condition (Union[Unset, int]): Condition is a range of 0 to 100 where 0 is completely worn out and 100 is brand
            new.
    """

    symbol: ShipReactorSymbol = Field(alias="symbol")
    name: str = Field(alias="name")
    description: str = Field(alias="description")
    power_output: int = Field(alias="powerOutput")
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
