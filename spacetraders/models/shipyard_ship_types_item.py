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

from ..models.ship_type import ShipType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ShipyardShipTypesItem")


@attr.s(auto_attribs=True)
class ShipyardShipTypesItem:
    """
    Attributes:
        type (Union[Unset, ShipType]):
    """

    type: Union[Unset, ShipType] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _type = d.pop("type", UNSET)
        type: Union[Unset, ShipType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = ShipType(_type)

        shipyard_ship_types_item = cls(
            type=type,
        )

        shipyard_ship_types_item.additional_properties = d
        return shipyard_ship_types_item

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
