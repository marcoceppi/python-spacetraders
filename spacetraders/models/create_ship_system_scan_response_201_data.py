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
    from ..models.scanned_system import ScannedSystem


T = TypeVar("T", bound="CreateShipSystemScanResponse201Data")


@attr.s(auto_attribs=True)
class CreateShipSystemScanResponse201Data:
    """
    Attributes:
        cooldown (Cooldown): A cooldown is a period of time in which a ship cannot perform certain actions.
        systems (List['ScannedSystem']):
    """

    cooldown: "Cooldown"
    systems: List["ScannedSystem"]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.cooldown import Cooldown
        from ..models.scanned_system import ScannedSystem

        cooldown = self.cooldown.to_dict()

        systems = []
        for systems_item_data in self.systems:
            systems_item = systems_item_data.to_dict()

            systems.append(systems_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "cooldown": cooldown,
                "systems": systems,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.cooldown import Cooldown
        from ..models.scanned_system import ScannedSystem

        d = src_dict.copy()
        cooldown = Cooldown.from_dict(d.pop("cooldown"))

        systems = []
        _systems = d.pop("systems")
        for systems_item_data in _systems:
            systems_item = ScannedSystem.from_dict(systems_item_data)

            systems.append(systems_item)

        create_ship_system_scan_response_201_data = cls(
            cooldown=cooldown,
            systems=systems,
        )

        create_ship_system_scan_response_201_data.additional_properties = d
        return create_ship_system_scan_response_201_data

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
