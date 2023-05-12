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

    trade_symbol: Union[Unset, str] = Field(UNSET, alias="tradeSymbol")
    units: Union[Unset, int] = Field(UNSET, alias="units")
    additional_properties: Dict[str, Any] = {}

    class Config:
        arbitrary_types_allowed = True
        allow_population_by_field_name = True

    def dict(self, *args, **kwargs):
        output = super().dict(*args, **kwargs)
        return {k: v for k, v in output.items() if v is not UNSET}

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
