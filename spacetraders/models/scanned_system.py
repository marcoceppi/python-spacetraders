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

from ..models.system_type import SystemType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ScannedSystem")


class ScannedSystem(BaseModel):
    """
    Attributes:
        symbol (str):
        sector_symbol (str):
        type (SystemType): The type of waypoint.
        x (int):
        y (int):
        distance (int):
    """

    symbol: str = Field(alias="symbol")
    sector_symbol: str = Field(alias="sectorSymbol")
    type: SystemType = Field(alias="type")
    x: int = Field(alias="x")
    y: int = Field(alias="y")
    distance: int = Field(alias="distance")
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
