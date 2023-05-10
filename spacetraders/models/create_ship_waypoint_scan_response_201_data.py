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

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cooldown import Cooldown
    from ..models.scanned_waypoint import ScannedWaypoint


T = TypeVar("T", bound="CreateShipWaypointScanResponse201Data")


@attr.s(auto_attribs=True)
class CreateShipWaypointScanResponse201Data:
    """
    Attributes:
        cooldown (Cooldown): A cooldown is a period of time in which a ship cannot perform certain actions.
        waypoints (List['ScannedWaypoint']):
    """

    cooldown: "Cooldown"
    waypoints: List["ScannedWaypoint"]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.cooldown import Cooldown
        from ..models.scanned_waypoint import ScannedWaypoint

        cooldown = self.cooldown.to_dict()

        waypoints = []
        for waypoints_item_data in self.waypoints:
            waypoints_item = waypoints_item_data.to_dict()

            waypoints.append(waypoints_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "cooldown": cooldown,
                "waypoints": waypoints,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.cooldown import Cooldown
        from ..models.scanned_waypoint import ScannedWaypoint

        d = src_dict.copy()
        cooldown = Cooldown.from_dict(d.pop("cooldown"))

        waypoints = []
        _waypoints = d.pop("waypoints")
        for waypoints_item_data in _waypoints:
            waypoints_item = ScannedWaypoint.from_dict(waypoints_item_data)

            waypoints.append(waypoints_item)

        create_ship_waypoint_scan_response_201_data = cls(
            cooldown=cooldown,
            waypoints=waypoints,
        )

        create_ship_waypoint_scan_response_201_data.additional_properties = d
        return create_ship_waypoint_scan_response_201_data

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
