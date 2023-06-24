from typing import (
    Any,
    Dict,
    List,
    TypeVar,
)

from pydantic import BaseModel, Field

from ..models.agent import Agent
from ..models.ship import Ship
from ..models.shipyard_transaction import ShipyardTransaction
from ..types import Unset

T = TypeVar("T", bound="PurchaseShipResponse201Data")


class PurchaseShipResponse201Data(BaseModel):
    """
    Attributes:
        agent (Agent): Agent details.
        ship (Ship): Ship details.
        transaction (ShipyardTransaction): Results of a transaction with a shipyard.
    """

    agent: "Agent" = Field(alias="agent")
    ship: "Ship" = Field(alias="ship")
    transaction: "ShipyardTransaction" = Field(alias="transaction")
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
