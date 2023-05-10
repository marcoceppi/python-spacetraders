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
    from ..models.faction import Faction
    from ..models.meta import Meta


T = TypeVar("T", bound="GetFactionsResponse200")


@attr.s(auto_attribs=True)
class GetFactionsResponse200:
    """
    Attributes:
        data (List['Faction']):
        meta (Meta):
    """

    data: List["Faction"]
    meta: "Meta"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.faction import Faction
        from ..models.meta import Meta

        data = []
        for data_item_data in self.data:
            data_item = data_item_data.to_dict()

            data.append(data_item)

        meta = self.meta.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data": data,
                "meta": meta,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.faction import Faction
        from ..models.meta import Meta

        d = src_dict.copy()
        data = []
        _data = d.pop("data")
        for data_item_data in _data:
            data_item = Faction.from_dict(data_item_data)

            data.append(data_item)

        meta = Meta.from_dict(d.pop("meta"))

        get_factions_response_200 = cls(
            data=data,
            meta=meta,
        )

        get_factions_response_200.additional_properties = d
        return get_factions_response_200

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
