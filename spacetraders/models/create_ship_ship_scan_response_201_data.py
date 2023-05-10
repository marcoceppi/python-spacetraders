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
    from ..models.scanned_ship import ScannedShip


T = TypeVar("T", bound="CreateShipShipScanResponse201Data")


@attr.s(auto_attribs=True)
class CreateShipShipScanResponse201Data:
    """
    Attributes:
        cooldown (Cooldown): A cooldown is a period of time in which a ship cannot perform certain actions.
        ships (List['ScannedShip']):
    """

    cooldown: "Cooldown"
    ships: List["ScannedShip"]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.cooldown import Cooldown
        from ..models.scanned_ship import ScannedShip

        cooldown = self.cooldown.to_dict()

        ships = []
        for ships_item_data in self.ships:
            ships_item = ships_item_data.to_dict()

            ships.append(ships_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "cooldown": cooldown,
                "ships": ships,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.cooldown import Cooldown
        from ..models.scanned_ship import ScannedShip

        d = src_dict.copy()
        cooldown = Cooldown.from_dict(d.pop("cooldown"))

        ships = []
        _ships = d.pop("ships")
        for ships_item_data in _ships:
            ships_item = ScannedShip.from_dict(ships_item_data)

            ships.append(ships_item)

        create_ship_ship_scan_response_201_data = cls(
            cooldown=cooldown,
            ships=ships,
        )

        create_ship_ship_scan_response_201_data.additional_properties = d
        return create_ship_ship_scan_response_201_data

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
