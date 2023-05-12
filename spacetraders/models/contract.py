import datetime
from typing import (
    Any,
    Dict,
    List,
    TypeVar,
)

from pydantic import BaseModel, Field

from ..models.contract_terms import ContractTerms
from ..models.contract_type import ContractType
from ..types import Unset

T = TypeVar("T", bound="Contract")


class Contract(BaseModel):
    """
    Attributes:
        id (str):
        faction_symbol (str): The symbol of the faction that this contract is for.
        type (ContractType):
        terms (ContractTerms):
        accepted (bool): Whether the contract has been accepted by the agent
        fulfilled (bool): Whether the contract has been fulfilled
        expiration (datetime.datetime): The time at which the contract expires
    """

    id: str = Field(alias="id")
    faction_symbol: str = Field(alias="factionSymbol")
    type: ContractType = Field(alias="type")
    terms: "ContractTerms" = Field(alias="terms")
    expiration: datetime.datetime = Field(alias="expiration")
    accepted: bool = Field(False, alias="accepted")
    fulfilled: bool = Field(False, alias="fulfilled")
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
