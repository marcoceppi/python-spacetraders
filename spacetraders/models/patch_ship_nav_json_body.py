from typing import (
    Any,
    Dict,
    List,
    TypeVar,
    Union,
)

from pydantic import BaseModel, Field

from ..models.ship_nav_flight_mode import ShipNavFlightMode
from ..types import Unset

T = TypeVar("T", bound="PatchShipNavJsonBody")


class PatchShipNavJsonBody(BaseModel):
    """
    Attributes:
        flight_mode (Union[Unset, ShipNavFlightMode]): The ship's set speed when traveling between waypoints or systems.
            Default: ShipNavFlightMode.CRUISE.
    """

    flight_mode: Union[Unset, ShipNavFlightMode] = Field(
        ShipNavFlightMode.CRUISE, alias="flightMode"
    )
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
