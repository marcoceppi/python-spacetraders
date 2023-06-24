from typing import (
    Any,
    Dict,
    List,
    TypeVar,
    Union,
)

from pydantic import BaseModel, Field

from ..models.chart import Chart
from ..models.waypoint_faction import WaypointFaction
from ..models.waypoint_orbital import WaypointOrbital
from ..models.waypoint_trait import WaypointTrait
from ..models.waypoint_type import WaypointType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ScannedWaypoint")


class ScannedWaypoint(BaseModel):
    """A waypoint that was scanned by a ship.

    Attributes:
        symbol (str): Symbol of the waypoint.
        type (WaypointType): The type of waypoint.
        system_symbol (str): Symbol of the system.
        x (int): Position in the universe in the x axis.
        y (int): Position in the universe in the y axis.
        orbitals (List['WaypointOrbital']): List of waypoints that orbit this waypoint.
        traits (List['WaypointTrait']): The traits of the waypoint.
        faction (Union[Unset, WaypointFaction]): The faction that controls the waypoint.
        chart (Union[Unset, Chart]): The chart of a system or waypoint, which makes the location visible to other
            agents.
    """

    symbol: str = Field(alias="symbol")
    type: WaypointType = Field(alias="type")
    system_symbol: str = Field(alias="systemSymbol")
    x: int = Field(alias="x")
    y: int = Field(alias="y")
    orbitals: List["WaypointOrbital"] = Field(alias="orbitals")
    traits: List["WaypointTrait"] = Field(alias="traits")
    faction: Union[Unset, "WaypointFaction"] = Field(UNSET, alias="faction")
    chart: Union[Unset, "Chart"] = Field(UNSET, alias="chart")
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
