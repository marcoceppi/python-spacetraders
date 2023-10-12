from typing import (
    Any,
    Dict,
    List,
    TypeVar,
    Union,
)

from pydantic import BaseModel, Field

from ..models.ship_engine import ShipEngine
from ..models.ship_frame import ShipFrame
from ..models.ship_module import ShipModule
from ..models.ship_mount import ShipMount
from ..models.ship_reactor import ShipReactor
from ..models.ship_type import ShipType
from ..models.shipyard_ship_crew import ShipyardShipCrew
from ..types import UNSET, Unset

T = TypeVar("T", bound="ShipyardShip")


class ShipyardShip(BaseModel):
    """
    Attributes:
        name (str):
        description (str):
        purchase_price (int):
        frame (ShipFrame): The frame of the ship. The frame determines the number of modules and mounting points of the
            ship, as well as base fuel capacity. As the condition of the frame takes more wear, the ship will become more
            sluggish and less maneuverable.
        reactor (ShipReactor): The reactor of the ship. The reactor is responsible for powering the ship's systems and
            weapons.
        engine (ShipEngine): The engine determines how quickly a ship travels between waypoints.
        modules (List['ShipModule']):
        mounts (List['ShipMount']):
        crew (ShipyardShipCrew):
        type (Union[Unset, ShipType]): Type of ship
    """

    name: str = Field(alias="name")
    description: str = Field(alias="description")
    purchase_price: int = Field(alias="purchasePrice")
    frame: "ShipFrame" = Field(alias="frame")
    reactor: "ShipReactor" = Field(alias="reactor")
    engine: "ShipEngine" = Field(alias="engine")
    modules: List["ShipModule"] = Field(alias="modules")
    mounts: List["ShipMount"] = Field(alias="mounts")
    crew: "ShipyardShipCrew" = Field(alias="crew")
    type: Union[Unset, ShipType] = Field(UNSET, alias="type")
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
