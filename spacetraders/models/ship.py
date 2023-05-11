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
from pydantic import BaseModel, Field

from ..models.ship_cargo import ShipCargo
from ..models.ship_crew import ShipCrew
from ..models.ship_engine import ShipEngine
from ..models.ship_frame import ShipFrame
from ..models.ship_fuel import ShipFuel
from ..models.ship_module import ShipModule
from ..models.ship_mount import ShipMount
from ..models.ship_nav import ShipNav
from ..models.ship_reactor import ShipReactor
from ..models.ship_registration import ShipRegistration
from ..types import UNSET, Unset

T = TypeVar("T", bound="Ship")


class Ship(BaseModel):
    """A ship

    Attributes:
        symbol (str): The globally unique identifier of the ship in the following format: `[AGENT_SYMBOL]_[HEX_ID]`
        registration (ShipRegistration): The public registration information of the ship
        nav (ShipNav): The navigation information of the ship.
        crew (ShipCrew): The ship's crew service and maintain the ship's systems and equipment.
        frame (ShipFrame): The frame of the ship. The frame determines the number of modules and mounting points of the
            ship, as well as base fuel capacity. As the condition of the frame takes more wear, the ship will become more
            sluggish and less maneuverable.
        reactor (ShipReactor): The reactor of the ship. The reactor is responsible for powering the ship's systems and
            weapons.
        engine (ShipEngine): The engine determines how quickly a ship travels between waypoints.
        modules (List['ShipModule']):
        mounts (List['ShipMount']):
        cargo (ShipCargo):
        fuel (ShipFuel): Details of the ship's fuel tanks including how much fuel was consumed during the last transit
            or action.
    """

    symbol: str = Field(alias="symbol")
    registration: "ShipRegistration" = Field(alias="registration")
    nav: "ShipNav" = Field(alias="nav")
    crew: "ShipCrew" = Field(alias="crew")
    frame: "ShipFrame" = Field(alias="frame")
    reactor: "ShipReactor" = Field(alias="reactor")
    engine: "ShipEngine" = Field(alias="engine")
    modules: List["ShipModule"] = Field(alias="modules")
    mounts: List["ShipMount"] = Field(alias="mounts")
    cargo: "ShipCargo" = Field(alias="cargo")
    fuel: "ShipFuel" = Field(alias="fuel")
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
