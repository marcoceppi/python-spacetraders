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
    from ..models.market_transaction import MarketTransaction
    from ..models.ship_cargo import ShipCargo


T = TypeVar("T", bound="SellCargoSellCargo201ResponseData")


@attr.s(auto_attribs=True)
class SellCargoSellCargo201ResponseData:
    """
    Attributes:
        agent (Agent):
        cargo (ShipCargo):
        transaction (MarketTransaction):
    """

    agent: "Agent"
    cargo: "ShipCargo"
    transaction: "MarketTransaction"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.agent import Agent
        from ..models.market_transaction import MarketTransaction
        from ..models.ship_cargo import ShipCargo

        agent = self.agent.to_dict()

        cargo = self.cargo.to_dict()

        transaction = self.transaction.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "agent": agent,
                "cargo": cargo,
                "transaction": transaction,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.agent import Agent
        from ..models.market_transaction import MarketTransaction
        from ..models.ship_cargo import ShipCargo

        d = src_dict.copy()
        agent = Agent.from_dict(d.pop("agent"))

        cargo = ShipCargo.from_dict(d.pop("cargo"))

        transaction = MarketTransaction.from_dict(d.pop("transaction"))

        sell_cargo_sell_cargo_201_response_data = cls(
            agent=agent,
            cargo=cargo,
            transaction=transaction,
        )

        sell_cargo_sell_cargo_201_response_data.additional_properties = d
        return sell_cargo_sell_cargo_201_response_data

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
