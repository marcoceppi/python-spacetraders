from typing import (
    Any,
    Dict,
    List,
    TypeVar,
)

from pydantic import BaseModel, Field

from ..models.system_faction import SystemFaction
from ..models.system_type import SystemType
from ..models.system_waypoint import SystemWaypoint
from ..types import Unset

T = TypeVar("T", bound="System")


class System(BaseModel):
    """
    Attributes:
        symbol (str): The symbol of the system.
        sector_symbol (str): The symbol of the sector.
        type (SystemType): The type of waypoint.
        x (int): Relative position of the system in the sector in the x axis.
        y (int): Relative position of the system in the sector in the y axis.
        waypoints (List['SystemWaypoint']): Waypoints in this system.
        factions (List['SystemFaction']): Factions that control this system.
    """

    symbol: str = Field(alias="symbol")
    sector_symbol: str = Field(alias="sectorSymbol")
    type: SystemType = Field(alias="type")
    x: int = Field(alias="x")
    y: int = Field(alias="y")
    waypoints: List["SystemWaypoint"] = Field(alias="waypoints")
    factions: List["SystemFaction"] = Field(alias="factions")
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
