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
    from ..models.faction_trait import FactionTrait


T = TypeVar("T", bound="Faction")


@attr.s(auto_attribs=True)
class Faction:
    """
    Attributes:
        symbol (str):
        name (str):
        description (str):
        headquarters (str):
        traits (List['FactionTrait']):
    """

    symbol: str
    name: str
    description: str
    headquarters: str
    traits: List["FactionTrait"]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.faction_trait import FactionTrait

        symbol = self.symbol
        name = self.name
        description = self.description
        headquarters = self.headquarters
        traits = []
        for traits_item_data in self.traits:
            traits_item = traits_item_data.to_dict()

            traits.append(traits_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "symbol": symbol,
                "name": name,
                "description": description,
                "headquarters": headquarters,
                "traits": traits,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.faction_trait import FactionTrait

        d = src_dict.copy()
        symbol = d.pop("symbol")

        name = d.pop("name")

        description = d.pop("description")

        headquarters = d.pop("headquarters")

        traits = []
        _traits = d.pop("traits")
        for traits_item_data in _traits:
            traits_item = FactionTrait.from_dict(traits_item_data)

            traits.append(traits_item)

        faction = cls(
            symbol=symbol,
            name=name,
            description=description,
            headquarters=headquarters,
            traits=traits,
        )

        faction.additional_properties = d
        return faction

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
