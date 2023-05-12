from typing import (
    Any,
    Dict,
    List,
    TypeVar,
)

from pydantic import BaseModel, Field

from ..models.ship_fuel import ShipFuel
from ..models.ship_nav import ShipNav
from ..types import Unset

T = TypeVar("T", bound="WarpShipResponse200Data")


class WarpShipResponse200Data(BaseModel):
    """
    Attributes:
        fuel (ShipFuel): Details of the ship's fuel tanks including how much fuel was consumed during the last transit
            or action.
        nav (ShipNav): The navigation information of the ship.
    """

    fuel: "ShipFuel" = Field(alias="fuel")
    nav: "ShipNav" = Field(alias="nav")
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
