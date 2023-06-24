from typing import (
    Any,
    Dict,
    List,
    TypeVar,
)

from pydantic import BaseModel, Field

from ..types import Unset

T = TypeVar("T", bound="GetStatusResponse200Stats")


class GetStatusResponse200Stats(BaseModel):
    """
    Attributes:
        agents (int): Number of registered agents in the game.
        ships (int): Total number of ships in the game.
        systems (int): Total number of systems in the game.
        waypoints (int): Total number of waypoints in the game.
    """

    agents: int = Field(alias="agents")
    ships: int = Field(alias="ships")
    systems: int = Field(alias="systems")
    waypoints: int = Field(alias="waypoints")
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
