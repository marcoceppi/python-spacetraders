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
from pydantic import BaseModel, Field

from ..models.ship_crew_rotation import ShipCrewRotation
from ..types import UNSET, Unset

T = TypeVar("T", bound="ShipCrew")


class ShipCrew(BaseModel):
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

    current: int = Field(alias="current")
    required: int = Field(alias="required")
    capacity: int = Field(alias="capacity")
    morale: int = Field(alias="morale")
    wages: int = Field(alias="wages")
    rotation: ShipCrewRotation = ShipCrewRotation.STRICT
    additional_properties: Dict[str, Any] = {}

    class Config:
        arbitrary_types_allowed = True

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
