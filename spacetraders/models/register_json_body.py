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

from ..models.register_json_body_faction import RegisterJsonBodyFaction
from ..types import UNSET, Unset

T = TypeVar("T", bound="RegisterJsonBody")


@attr.s(auto_attribs=True)
class RegisterJsonBody:
    """
    Attributes:
        faction (RegisterJsonBodyFaction): The faction you choose determines your headquarters.
        symbol (str): How other agents will see your ships and information. Example: BADGER.
    """

    faction: RegisterJsonBodyFaction
    symbol: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        faction = self.faction.value

        symbol = self.symbol

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "faction": faction,
                "symbol": symbol,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        faction = RegisterJsonBodyFaction(d.pop("faction"))

        symbol = d.pop("symbol")

        register_json_body = cls(
            faction=faction,
            symbol=symbol,
        )

        register_json_body.additional_properties = d
        return register_json_body

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
