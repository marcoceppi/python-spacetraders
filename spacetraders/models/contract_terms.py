import datetime
from typing import (
    TYPE_CHECKING,
    Any,
    BinaryIO,
    Dict,
    List,
    Optional,
    TextIO,
    Tuple,
    Type,
    TypeVar,
    Union,
    cast,
)

import attr
from dateutil.parser import isoparse
from pydantic import BaseModel, Field

from ..models.contract_deliver_good import ContractDeliverGood
from ..models.contract_payment import ContractPayment
from ..types import UNSET, Unset

T = TypeVar("T", bound="ContractTerms")


class ContractTerms(BaseModel):
    """
    Attributes:
        deadline (datetime.datetime): The deadline for the contract.
        payment (ContractPayment):
        deliver (Union[Unset, List['ContractDeliverGood']]):
    """

    deadline: datetime.datetime = Field(alias="deadline")
    payment: "ContractPayment" = Field(alias="payment")
    deliver: Union[Unset, List["ContractDeliverGood"]] = UNSET
    additional_properties: Dict[str, Any] = {}

    class Config:
        arbitrary_types_allowed = True

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
