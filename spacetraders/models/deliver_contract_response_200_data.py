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
    cast,
)

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.contract import Contract
    from ..models.ship_cargo import ShipCargo


T = TypeVar("T", bound="DeliverContractResponse200Data")


@attr.s(auto_attribs=True)
class DeliverContractResponse200Data:
    """
    Attributes:
        contract (Contract):
        cargo (ShipCargo):
    """

    contract: "Contract"
    cargo: "ShipCargo"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.contract import Contract
        from ..models.ship_cargo import ShipCargo

        contract = self.contract.to_dict()

        cargo = self.cargo.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "contract": contract,
                "cargo": cargo,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.contract import Contract
        from ..models.ship_cargo import ShipCargo

        d = src_dict.copy()
        contract = Contract.from_dict(d.pop("contract"))

        cargo = ShipCargo.from_dict(d.pop("cargo"))

        deliver_contract_response_200_data = cls(
            contract=contract,
            cargo=cargo,
        )

        deliver_contract_response_200_data.additional_properties = d
        return deliver_contract_response_200_data

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
