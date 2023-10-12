from typing import (
    Any,
    Dict,
    List,
    TypeVar,
)

from pydantic import BaseModel, Field

from ..models.extract_resources_with_survey_response_201_data import (
    ExtractResourcesWithSurveyResponse201Data,
)
from ..types import Unset

T = TypeVar("T", bound="ExtractResourcesWithSurveyResponse201")


class ExtractResourcesWithSurveyResponse201(BaseModel):
    """
    Attributes:
        data (ExtractResourcesWithSurveyResponse201Data):
    """

    data: "ExtractResourcesWithSurveyResponse201Data" = Field(alias="data")
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
