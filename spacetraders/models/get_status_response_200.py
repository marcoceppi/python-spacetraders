from typing import (
    Any,
    Dict,
    List,
    TypeVar,
)

from pydantic import BaseModel, Field

from ..models.get_status_response_200_announcements_item import (
    GetStatusResponse200AnnouncementsItem,
)
from ..models.get_status_response_200_leaderboards import (
    GetStatusResponse200Leaderboards,
)
from ..models.get_status_response_200_links_item import GetStatusResponse200LinksItem
from ..models.get_status_response_200_server_resets import (
    GetStatusResponse200ServerResets,
)
from ..models.get_status_response_200_stats import GetStatusResponse200Stats
from ..types import Unset

T = TypeVar("T", bound="GetStatusResponse200")


class GetStatusResponse200(BaseModel):
    """
    Attributes:
        status (str): The current status of the game server.
        version (str): The current version of the API.
        reset_date (str): The date when the game server was last reset.
        description (str):
        stats (GetStatusResponse200Stats):
        leaderboards (GetStatusResponse200Leaderboards):
        server_resets (GetStatusResponse200ServerResets):
        announcements (List['GetStatusResponse200AnnouncementsItem']):
        links (List['GetStatusResponse200LinksItem']):
    """

    status: str = Field(alias="status")
    version: str = Field(alias="version")
    reset_date: str = Field(alias="resetDate")
    description: str = Field(alias="description")
    stats: "GetStatusResponse200Stats" = Field(alias="stats")
    leaderboards: "GetStatusResponse200Leaderboards" = Field(alias="leaderboards")
    server_resets: "GetStatusResponse200ServerResets" = Field(alias="serverResets")
    announcements: List["GetStatusResponse200AnnouncementsItem"] = Field(
        alias="announcements"
    )
    links: List["GetStatusResponse200LinksItem"] = Field(alias="links")
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
