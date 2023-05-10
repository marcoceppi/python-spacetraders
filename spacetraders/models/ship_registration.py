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
    Union,
)

import attr

from ..models.ship_role import ShipRole
from ..types import UNSET, Unset

T = TypeVar("T", bound="ShipRegistration")


@attr.s(auto_attribs=True)
class ShipRegistration:
    """The public registration information of the ship

    Attributes:
        name (str): The agent's registered name of the ship
        role (ShipRole): The registered role of the ship
        faction_symbol (Union[Unset, str]): The symbol of the faction the ship is registered with
    """

    name: str
    role: ShipRole
    faction_symbol: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        role = self.role.value

        faction_symbol = self.faction_symbol

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "role": role,
            }
        )
        if faction_symbol is not UNSET:
            field_dict["factionSymbol"] = faction_symbol

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        role = ShipRole(d.pop("role"))

        faction_symbol = d.pop("factionSymbol", UNSET)

        ship_registration = cls(
            name=name,
            role=role,
            faction_symbol=faction_symbol,
        )

        ship_registration.additional_properties = d
        return ship_registration

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
