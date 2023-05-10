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
)

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ContractPayment")


@attr.s(auto_attribs=True)
class ContractPayment:
    """
    Attributes:
        on_accepted (int): The amount of credits received up front for accepting the contract.
        on_fulfilled (int): The amount of credits received when the contract is fulfilled.
    """

    on_accepted: int
    on_fulfilled: int
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        on_accepted = self.on_accepted
        on_fulfilled = self.on_fulfilled

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "onAccepted": on_accepted,
                "onFulfilled": on_fulfilled,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        on_accepted = d.pop("onAccepted")

        on_fulfilled = d.pop("onFulfilled")

        contract_payment = cls(
            on_accepted=on_accepted,
            on_fulfilled=on_fulfilled,
        )

        contract_payment.additional_properties = d
        return contract_payment

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
