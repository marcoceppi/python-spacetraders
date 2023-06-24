import datetime
from typing import (
    Any,
    Dict,
    List,
    TypeVar,
    Union,
)

from pydantic import BaseModel, Field

from ..models.contract_deliver_good import ContractDeliverGood
from ..models.contract_payment import ContractPayment
from ..types import UNSET, Unset

T = TypeVar("T", bound="ContractTerms")


class ContractTerms(BaseModel):
    """Terms of the contract needed to fulfill it.

    Attributes:
        deadline (datetime.datetime): The deadline for the contract.
        payment (ContractPayment):
        deliver (Union[Unset, List['ContractDeliverGood']]): The cargo that needs to be delivered to fulfill the
            contract.
    """

    deadline: datetime.datetime = Field(alias="deadline")
    payment: "ContractPayment" = Field(alias="payment")
    deliver: Union[Unset, List["ContractDeliverGood"]] = Field(UNSET, alias="deliver")
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
