from typing import (
    Any,
    Dict,
    List,
    TypeVar,
)

from pydantic import BaseModel, Field

from ..types import Unset

T = TypeVar("T", bound="ContractDeliverGood")


class ContractDeliverGood(BaseModel):
    """The details of a delivery contract. Includes the type of good, units needed, and the destination.

    Attributes:
        trade_symbol (str): The symbol of the trade good to deliver.
        destination_symbol (str): The destination where goods need to be delivered.
        units_required (int): The number of units that need to be delivered on this contract.
        units_fulfilled (int): The number of units fulfilled on this contract.
    """

    trade_symbol: str = Field(alias="tradeSymbol")
    destination_symbol: str = Field(alias="destinationSymbol")
    units_required: int = Field(alias="unitsRequired")
    units_fulfilled: int = Field(alias="unitsFulfilled")
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
