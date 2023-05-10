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

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.contract_deliver_good import ContractDeliverGood
    from ..models.contract_payment import ContractPayment


T = TypeVar("T", bound="ContractTerms")


@attr.s(auto_attribs=True)
class ContractTerms:
    """
    Attributes:
        deadline (datetime.datetime): The deadline for the contract.
        payment (ContractPayment):
        deliver (Union[Unset, List['ContractDeliverGood']]):
    """

    deadline: datetime.datetime
    payment: "ContractPayment"
    deliver: Union[Unset, List["ContractDeliverGood"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.contract_deliver_good import ContractDeliverGood
        from ..models.contract_payment import ContractPayment

        deadline = self.deadline.isoformat()

        payment = self.payment.to_dict()

        deliver: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.deliver, Unset):
            deliver = []
            for deliver_item_data in self.deliver:
                deliver_item = deliver_item_data.to_dict()

                deliver.append(deliver_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "deadline": deadline,
                "payment": payment,
            }
        )
        if deliver is not UNSET:
            field_dict["deliver"] = deliver

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.contract_deliver_good import ContractDeliverGood
        from ..models.contract_payment import ContractPayment

        d = src_dict.copy()
        deadline = isoparse(d.pop("deadline"))

        payment = ContractPayment.from_dict(d.pop("payment"))

        deliver = []
        _deliver = d.pop("deliver", UNSET)
        for deliver_item_data in _deliver or []:
            deliver_item = ContractDeliverGood.from_dict(deliver_item_data)

            deliver.append(deliver_item)

        contract_terms = cls(
            deadline=deadline,
            payment=payment,
            deliver=deliver,
        )

        contract_terms.additional_properties = d
        return contract_terms

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
