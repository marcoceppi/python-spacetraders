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
    from ..models.waypoint import Waypoint


T = TypeVar("T", bound="GetWaypointResponse200")


@attr.s(auto_attribs=True)
class GetWaypointResponse200:
    """
    Attributes:
        data (Waypoint): A waypoint is a location that ships can travel to such as a Planet, Moon or Space Station.
    """

    data: "Waypoint"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.waypoint import Waypoint

        data = self.data.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data": data,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.waypoint import Waypoint

        d = src_dict.copy()
        data = Waypoint.from_dict(d.pop("data"))

        get_waypoint_response_200 = cls(
            data=data,
        )

        get_waypoint_response_200.additional_properties = d
        return get_waypoint_response_200

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
