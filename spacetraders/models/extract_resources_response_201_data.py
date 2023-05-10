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
    from ..models.extraction import Extraction
    from ..models.ship_cargo import ShipCargo


T = TypeVar("T", bound="ExtractResourcesResponse201Data")


@attr.s(auto_attribs=True)
class ExtractResourcesResponse201Data:
    """
    Attributes:
        cooldown (Cooldown): A cooldown is a period of time in which a ship cannot perform certain actions.
        extraction (Extraction):
        cargo (ShipCargo):
    """

    cooldown: "Cooldown"
    extraction: "Extraction"
    cargo: "ShipCargo"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.cooldown import Cooldown
        from ..models.extraction import Extraction
        from ..models.ship_cargo import ShipCargo

        cooldown = self.cooldown.to_dict()

        extraction = self.extraction.to_dict()

        cargo = self.cargo.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "cooldown": cooldown,
                "extraction": extraction,
                "cargo": cargo,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.cooldown import Cooldown
        from ..models.extraction import Extraction
        from ..models.ship_cargo import ShipCargo

        d = src_dict.copy()
        cooldown = Cooldown.from_dict(d.pop("cooldown"))

        extraction = Extraction.from_dict(d.pop("extraction"))

        cargo = ShipCargo.from_dict(d.pop("cargo"))

        extract_resources_response_201_data = cls(
            cooldown=cooldown,
            extraction=extraction,
            cargo=cargo,
        )

        extract_resources_response_201_data.additional_properties = d
        return extract_resources_response_201_data

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
