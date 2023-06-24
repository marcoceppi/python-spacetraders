from typing import (
    Any,
    Dict,
    List,
    TypeVar,
)

from pydantic import BaseModel, Field

from ..models.faction_symbols import FactionSymbols
from ..models.faction_trait import FactionTrait
from ..types import Unset

T = TypeVar("T", bound="Faction")


class Faction(BaseModel):
    """Faction details.

    Attributes:
        symbol (FactionSymbols): The symbol of the faction.
        name (str): Name of the faction.
        description (str): Description of the faction.
        headquarters (str): The waypoint in which the faction's HQ is located in.
        traits (List['FactionTrait']): List of traits that define this faction.
        is_recruiting (bool): Whether or not the faction is currently recruiting new agents.
    """

    symbol: FactionSymbols = Field(alias="symbol")
    name: str = Field(alias="name")
    description: str = Field(alias="description")
    headquarters: str = Field(alias="headquarters")
    traits: List["FactionTrait"] = Field(alias="traits")
    is_recruiting: bool = Field(alias="isRecruiting")
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
