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

from ..models.ship_refine_json_body_produce import ShipRefineJsonBodyProduce
from ..types import UNSET, Unset

T = TypeVar("T", bound="ShipRefineJsonBody")


@attr.s(auto_attribs=True)
class ShipRefineJsonBody:
    """
    Attributes:
        produce (ShipRefineJsonBodyProduce):
    """

    produce: ShipRefineJsonBodyProduce
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        produce = self.produce.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "produce": produce,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        produce = ShipRefineJsonBodyProduce(d.pop("produce"))

        ship_refine_json_body = cls(
            produce=produce,
        )

        ship_refine_json_body.additional_properties = d
        return ship_refine_json_body

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
