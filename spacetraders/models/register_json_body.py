from typing import (
    Any,
    Dict,
    List,
    TypeVar,
    Union,
)

from pydantic import BaseModel, Field

from ..models.faction_symbols import FactionSymbols
from ..types import UNSET, Unset

T = TypeVar("T", bound="RegisterJsonBody")


class RegisterJsonBody(BaseModel):
    """
    Attributes:
        faction (FactionSymbols): The symbol of the faction.
        symbol (str): Your desired agent symbol. This will be a unique name used to represent your agent, and will be
            the prefix for your ships. Example: BADGER.
        email (Union[Unset, str]): Your email address. This is used if you reserved your call sign between resets.
    """

    faction: FactionSymbols = Field(alias="faction")
    symbol: str = Field(alias="symbol")
    email: Union[Unset, str] = Field(UNSET, alias="email")
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
