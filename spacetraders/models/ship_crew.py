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
)

import attr

from ..models.ship_crew_rotation import ShipCrewRotation
from ..types import UNSET, Unset

T = TypeVar("T", bound="ShipCrew")


@attr.s(auto_attribs=True)
class ShipCrew:
    """The ship's crew service and maintain the ship's systems and equipment.

    Attributes:
        current (int): The current number of crew members on the ship.
        required (int): The minimum number of crew members required to maintain the ship.
        capacity (int): The maximum number of crew members the ship can support.
        rotation (ShipCrewRotation): The rotation of crew shifts. A stricter shift improves the ship's performance. A
            more relaxed shift improves the crew's morale. Default: ShipCrewRotation.STRICT.
        morale (int): A rough measure of the crew's morale. A higher morale means the crew is happier and more
            productive. A lower morale means the ship is more prone to accidents.
        wages (int): The amount of credits per crew member paid per hour. Wages are paid when a ship docks at a
            civilized waypoint.
    """

    current: int
    required: int
    capacity: int
    morale: int
    wages: int
    rotation: ShipCrewRotation = ShipCrewRotation.STRICT
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        current = self.current
        required = self.required
        capacity = self.capacity
        rotation = self.rotation.value

        morale = self.morale
        wages = self.wages

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "current": current,
                "required": required,
                "capacity": capacity,
                "rotation": rotation,
                "morale": morale,
                "wages": wages,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        current = d.pop("current")

        required = d.pop("required")

        capacity = d.pop("capacity")

        rotation = ShipCrewRotation(d.pop("rotation"))

        morale = d.pop("morale")

        wages = d.pop("wages")

        ship_crew = cls(
            current=current,
            required=required,
            capacity=capacity,
            rotation=rotation,
            morale=morale,
            wages=wages,
        )

        ship_crew.additional_properties = d
        return ship_crew

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
