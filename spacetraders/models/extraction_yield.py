from typing import (
    Any,
    Dict,
    List,
    TypeVar,
)

from pydantic import BaseModel, Field

from ..models.trade_symbol import TradeSymbol
from ..types import Unset

T = TypeVar("T", bound="ExtractionYield")


class ExtractionYield(BaseModel):
    """A yield from the extraction operation.

    Attributes:
        symbol (TradeSymbol): The good's symbol.
        units (int): The number of units extracted that were placed into the ship's cargo hold.
    """

    symbol: TradeSymbol = Field(alias="symbol")
    units: int = Field(alias="units")
    additional_properties: Dict[str, Any] = {}

    class Config:
        arbitrary_types_allowed = True
        allow_population_by_field_name = True

    def dict(self, *args, **kwargs):
        output = super().dict(*args, **kwargs)
        return {k: v for k, v in output.items() if not isinstance(v, Unset)}

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
