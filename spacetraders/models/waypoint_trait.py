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

from ..models.waypoint_trait_symbol import WaypointTraitSymbol
from ..types import UNSET, Unset

T = TypeVar("T", bound="WaypointTrait")


class WaypointTrait(BaseModel):
    """
    Attributes:
        symbol (WaypointTraitSymbol): The unique identifier of the trait.
        name (str): The name of the trait.
        description (str): A description of the trait.
    """

    symbol: WaypointTraitSymbol = Field(alias="symbol")
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
