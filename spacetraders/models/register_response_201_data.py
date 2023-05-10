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
    from ..models.faction import Faction
    from ..models.ship import Ship


T = TypeVar("T", bound="RegisterResponse201Data")


@attr.s(auto_attribs=True)
class RegisterResponse201Data:
    """
    Attributes:
        agent (Agent):
        contract (Contract):
        faction (Faction):
        ship (Ship): A ship
        token (str): A Bearer token for accessing secured API endpoints.
    """

    agent: "Agent"
    contract: "Contract"
    faction: "Faction"
    ship: "Ship"
    token: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.agent import Agent
        from ..models.contract import Contract
        from ..models.faction import Faction
        from ..models.ship import Ship

        agent = self.agent.to_dict()

        contract = self.contract.to_dict()

        faction = self.faction.to_dict()

        ship = self.ship.to_dict()

        token = self.token

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "agent": agent,
                "contract": contract,
                "faction": faction,
                "ship": ship,
                "token": token,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.agent import Agent
        from ..models.contract import Contract
        from ..models.faction import Faction
        from ..models.ship import Ship

        d = src_dict.copy()
        agent = Agent.from_dict(d.pop("agent"))

        contract = Contract.from_dict(d.pop("contract"))

        faction = Faction.from_dict(d.pop("faction"))

        ship = Ship.from_dict(d.pop("ship"))

        token = d.pop("token")

        register_response_201_data = cls(
            agent=agent,
            contract=contract,
            faction=faction,
            ship=ship,
            token=token,
        )

        register_response_201_data.additional_properties = d
        return register_response_201_data

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
