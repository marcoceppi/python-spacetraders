from typing import (
    Any,
    Dict,
    List,
    TypeVar,
)

from pydantic import BaseModel, Field

from ..models.get_status_response_200_leaderboards_most_credits_item import (
    GetStatusResponse200LeaderboardsMostCreditsItem,
)
from ..models.get_status_response_200_leaderboards_most_submitted_charts_item import (
    GetStatusResponse200LeaderboardsMostSubmittedChartsItem,
)
from ..types import Unset

T = TypeVar("T", bound="GetStatusResponse200Leaderboards")


class GetStatusResponse200Leaderboards(BaseModel):
    """
    Attributes:
        most_credits (List['GetStatusResponse200LeaderboardsMostCreditsItem']): Top agents with the most credits.
        most_submitted_charts (List['GetStatusResponse200LeaderboardsMostSubmittedChartsItem']): Top agents with the
            most charted submitted.
    """

    most_credits: List["GetStatusResponse200LeaderboardsMostCreditsItem"] = Field(
        alias="mostCredits"
    )
    most_submitted_charts: List[
        "GetStatusResponse200LeaderboardsMostSubmittedChartsItem"
    ] = Field(alias="mostSubmittedCharts")
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
