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

from ..models.register_json_body_faction import RegisterJsonBodyFaction
from ..types import UNSET, Unset

T = TypeVar("T", bound="RegisterJsonBody")


class RegisterJsonBody(BaseModel):
    """
    Attributes:
        faction (RegisterJsonBodyFaction): The faction you choose determines your headquarters.
        symbol (str): How other agents will see your ships and information. Example: BADGER.
    """

    faction: RegisterJsonBodyFaction = Field(alias="faction")
    symbol: str = Field(alias="symbol")
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
