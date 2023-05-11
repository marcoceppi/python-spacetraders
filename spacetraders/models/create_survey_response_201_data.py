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
from pydantic import BaseModel, Field

from ..models.cooldown import Cooldown
from ..models.survey import Survey
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateSurveyResponse201Data")


class CreateSurveyResponse201Data(BaseModel):
    """
    Attributes:
        cooldown (Cooldown): A cooldown is a period of time in which a ship cannot perform certain actions.
        surveys (List['Survey']):
    """

    cooldown: "Cooldown" = Field(alias="cooldown")
    surveys: List["Survey"] = Field(alias="surveys")
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
