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
from pydantic import BaseModel, Field

from ..models.trade_symbol import TradeSymbol
from ..types import UNSET, Unset

T = TypeVar("T", bound="TradeGood")


class TradeGood(BaseModel):
    """
    Attributes:
        symbol (TradeSymbol):
        name (str):
        description (str):
    """

    symbol: TradeSymbol = Field(alias="symbol")
    name: str = Field(alias="name")
    description: str = Field(alias="description")
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
