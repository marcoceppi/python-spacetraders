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
from pydantic import BaseModel, Field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ShipRefineShipRefine200ResponseDataProducedItem")


class ShipRefineShipRefine200ResponseDataProducedItem(BaseModel):
    """
    Attributes:
        trade_symbol (Union[Unset, str]):
        units (Union[Unset, int]):
    """

    trade_symbol: Union[Unset, str] = UNSET
    units: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = {}

    class Config:
        arbitrary_types_allowed = True

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
