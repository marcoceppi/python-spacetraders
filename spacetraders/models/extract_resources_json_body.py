from typing import (
    Any,
    Dict,
    List,
    TypeVar,
    Union,
)

from pydantic import BaseModel, Field

from ..models.survey import Survey
from ..types import UNSET, Unset

T = TypeVar("T", bound="ExtractResourcesJsonBody")


class ExtractResourcesJsonBody(BaseModel):
    """
    Attributes:
        survey (Union[Unset, Survey]): A resource survey of a waypoint, detailing a specific extraction location and the
            types of resources that can be found there.
    """

    survey: Union[Unset, "Survey"] = Field(UNSET, alias="survey")
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
