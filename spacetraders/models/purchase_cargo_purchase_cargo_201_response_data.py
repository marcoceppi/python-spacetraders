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
from pydantic import BaseModel, Field

from ..models.agent import Agent
from ..models.market_transaction import MarketTransaction
from ..models.ship_cargo import ShipCargo
from ..types import UNSET, Unset

T = TypeVar("T", bound="PurchaseCargoPurchaseCargo201ResponseData")


class PurchaseCargoPurchaseCargo201ResponseData(BaseModel):
    """
    Attributes:
        agent (Agent):
        cargo (ShipCargo):
        transaction (MarketTransaction):
    """

    agent: "Agent" = Field(alias="agent")
    cargo: "ShipCargo" = Field(alias="cargo")
    transaction: "MarketTransaction" = Field(alias="transaction")
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
