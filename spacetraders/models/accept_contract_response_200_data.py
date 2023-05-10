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
    from ..models.agent import Agent
    from ..models.contract import Contract


T = TypeVar("T", bound="AcceptContractResponse200Data")


@attr.s(auto_attribs=True)
class AcceptContractResponse200Data:
    """
    Attributes:
        agent (Agent):
        contract (Contract):
    """

    agent: "Agent"
    contract: "Contract"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.agent import Agent
        from ..models.contract import Contract

        agent = self.agent.to_dict()

        contract = self.contract.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "agent": agent,
                "contract": contract,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.agent import Agent
        from ..models.contract import Contract

        d = src_dict.copy()
        agent = Agent.from_dict(d.pop("agent"))

        contract = Contract.from_dict(d.pop("contract"))

        accept_contract_response_200_data = cls(
            agent=agent,
            contract=contract,
        )

        accept_contract_response_200_data.additional_properties = d
        return accept_contract_response_200_data

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
