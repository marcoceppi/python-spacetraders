from typing import (
    Any,
    Dict,
    List,
    TypeVar,
    Union,
)

from pydantic import BaseModel, Field

from ..models.scanned_ship_engine import ScannedShipEngine
from ..models.scanned_ship_frame import ScannedShipFrame
from ..models.scanned_ship_mounts_item import ScannedShipMountsItem
from ..models.scanned_ship_reactor import ScannedShipReactor
from ..models.ship_nav import ShipNav
from ..models.ship_registration import ShipRegistration
from ..types import UNSET, Unset

T = TypeVar("T", bound="ScannedShip")


class ScannedShip(BaseModel):
    """The ship that was scanned. Details include information about the ship that could be detected by the scanner.

    Attributes:
        symbol (str): The globally unique identifier of the ship.
        registration (ShipRegistration): The public registration information of the ship
        nav (ShipNav): The navigation information of the ship.
        engine (ScannedShipEngine): The engine of the ship.
        frame (Union[Unset, ScannedShipFrame]): The frame of the ship.
        reactor (Union[Unset, ScannedShipReactor]): The reactor of the ship.
        mounts (Union[Unset, List['ScannedShipMountsItem']]): List of mounts installed in the ship.
    """

    symbol: str = Field(alias="symbol")
    registration: "ShipRegistration" = Field(alias="registration")
    nav: "ShipNav" = Field(alias="nav")
    engine: "ScannedShipEngine" = Field(alias="engine")
    frame: Union[Unset, "ScannedShipFrame"] = Field(UNSET, alias="frame")
    reactor: Union[Unset, "ScannedShipReactor"] = Field(UNSET, alias="reactor")
    mounts: Union[Unset, List["ScannedShipMountsItem"]] = Field(UNSET, alias="mounts")
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
