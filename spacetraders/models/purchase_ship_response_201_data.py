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
    from ..models.ship import Ship
    from ..models.shipyard_transaction import ShipyardTransaction


T = TypeVar("T", bound="PurchaseShipResponse201Data")


@attr.s(auto_attribs=True)
class PurchaseShipResponse201Data:
    """
    Attributes:
        agent (Agent):
        ship (Ship): A ship
        transaction (ShipyardTransaction):
    """

    agent: "Agent"
    ship: "Ship"
    transaction: "ShipyardTransaction"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.agent import Agent
        from ..models.ship import Ship
        from ..models.shipyard_transaction import ShipyardTransaction

        agent = self.agent.to_dict()

        ship = self.ship.to_dict()

        transaction = self.transaction.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "agent": agent,
                "ship": ship,
                "transaction": transaction,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.agent import Agent
        from ..models.ship import Ship
        from ..models.shipyard_transaction import ShipyardTransaction

        d = src_dict.copy()
        agent = Agent.from_dict(d.pop("agent"))

        ship = Ship.from_dict(d.pop("ship"))

        transaction = ShipyardTransaction.from_dict(d.pop("transaction"))

        purchase_ship_response_201_data = cls(
            agent=agent,
            ship=ship,
            transaction=transaction,
        )

        purchase_ship_response_201_data.additional_properties = d
        return purchase_ship_response_201_data

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
