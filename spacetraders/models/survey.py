import datetime
from typing import (
    Any,
    Dict,
    List,
    TypeVar,
)

from pydantic import BaseModel, Field

from ..models.survey_deposit import SurveyDeposit
from ..models.survey_size import SurveySize
from ..types import Unset

T = TypeVar("T", bound="Survey")


class Survey(BaseModel):
    """A resource survey of a waypoint, detailing a specific extraction location and the types of resources that can be
    found there.

        Attributes:
            signature (str): A unique signature for the location of this survey. This signature is verified when attempting
                an extraction using this survey.
            symbol (str): The symbol of the waypoint that this survey is for.
            deposits (List['SurveyDeposit']): A list of deposits that can be found at this location. A ship will extract one
                of these deposits when using this survey in an extraction request. If multiple deposits of the same type are
                present, the chance of extracting that deposit is increased.
            expiration (datetime.datetime): The date and time when the survey expires. After this date and time, the survey
                will no longer be available for extraction.
            size (SurveySize): The size of the deposit. This value indicates how much can be extracted from the survey
                before it is exhausted.
    """

    signature: str = Field(alias="signature")
    symbol: str = Field(alias="symbol")
    deposits: List["SurveyDeposit"] = Field(alias="deposits")
    expiration: datetime.datetime = Field(alias="expiration")
    size: SurveySize = Field(alias="size")
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
