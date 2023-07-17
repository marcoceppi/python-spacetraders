from typing import (
    Any,
    Dict,
    List,
    TypeVar,
    Union,
)

from pydantic import BaseModel, Field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Agent")


class Agent(BaseModel):
    """Agent details.

    Attributes:
        symbol (str): Symbol of the agent.
        headquarters (str): The headquarters of the agent.
        credits_ (int): The number of credits the agent has available. Credits can be negative if funds have been
            overdrawn.
        starting_faction (str): The faction the agent started with.
        account_id (Union[Unset, str]): Account ID that is tied to this agent. Only included on your own agent.
        ship_count (Union[Unset, int]): How many ships are owned by the agent.
    """

    symbol: str = Field(alias="symbol")
    headquarters: str = Field(alias="headquarters")
    credits_: int = Field(alias="credits")
    starting_faction: str = Field(alias="startingFaction")
    account_id: Union[Unset, str] = Field(UNSET, alias="accountId")
    ship_count: Union[Unset, int] = Field(UNSET, alias="shipCount")
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
