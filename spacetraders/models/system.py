from typing import (
    TYPE_CHECKING,
    Any,
    BinaryIO,
    Dict,
    List,
    Optional,
    TextIO,
    Tuple,
    Type,
    TypeVar,
    cast,
)

import attr

from ..models.system_type import SystemType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.system_faction import SystemFaction
    from ..models.system_waypoint import SystemWaypoint


T = TypeVar("T", bound="System")


@attr.s(auto_attribs=True)
class System:
    """
    Attributes:
        symbol (str):
        sector_symbol (str):
        type (SystemType): The type of waypoint.
        x (int):
        y (int):
        waypoints (List['SystemWaypoint']):
        factions (List['SystemFaction']):
    """

    symbol: str
    sector_symbol: str
    type: SystemType
    x: int
    y: int
    waypoints: List["SystemWaypoint"]
    factions: List["SystemFaction"]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.system_faction import SystemFaction
        from ..models.system_waypoint import SystemWaypoint

        symbol = self.symbol
        sector_symbol = self.sector_symbol
        type = self.type.value

        x = self.x
        y = self.y
        waypoints = []
        for waypoints_item_data in self.waypoints:
            waypoints_item = waypoints_item_data.to_dict()

            waypoints.append(waypoints_item)

        factions = []
        for factions_item_data in self.factions:
            factions_item = factions_item_data.to_dict()

            factions.append(factions_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "symbol": symbol,
                "sectorSymbol": sector_symbol,
                "type": type,
                "x": x,
                "y": y,
                "waypoints": waypoints,
                "factions": factions,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.system_faction import SystemFaction
        from ..models.system_waypoint import SystemWaypoint

        d = src_dict.copy()
        symbol = d.pop("symbol")

        sector_symbol = d.pop("sectorSymbol")

        type = SystemType(d.pop("type"))

        x = d.pop("x")

        y = d.pop("y")

        waypoints = []
        _waypoints = d.pop("waypoints")
        for waypoints_item_data in _waypoints:
            waypoints_item = SystemWaypoint.from_dict(waypoints_item_data)

            waypoints.append(waypoints_item)

        factions = []
        _factions = d.pop("factions")
        for factions_item_data in _factions:
            factions_item = SystemFaction.from_dict(factions_item_data)

            factions.append(factions_item)

        system = cls(
            symbol=symbol,
            sector_symbol=sector_symbol,
            type=type,
            x=x,
            y=y,
            waypoints=waypoints,
            factions=factions,
        )

        system.additional_properties = d
        return system

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
