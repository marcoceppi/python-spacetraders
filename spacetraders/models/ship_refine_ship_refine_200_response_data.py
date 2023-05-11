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

from ..models.cooldown import Cooldown
from ..models.ship_cargo import ShipCargo
from ..models.ship_refine_ship_refine_200_response_data_consumed_item import (
    ShipRefineShipRefine200ResponseDataConsumedItem,
)
from ..models.ship_refine_ship_refine_200_response_data_produced_item import (
    ShipRefineShipRefine200ResponseDataProducedItem,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ShipRefineShipRefine200ResponseData")


class ShipRefineShipRefine200ResponseData(BaseModel):
    """
    Attributes:
        cargo (ShipCargo):
        cooldown (Cooldown): A cooldown is a period of time in which a ship cannot perform certain actions.
        produced (List['ShipRefineShipRefine200ResponseDataProducedItem']):
        consumed (List['ShipRefineShipRefine200ResponseDataConsumedItem']):
    """

    cargo: "ShipCargo" = Field(alias="cargo")
    cooldown: "Cooldown" = Field(alias="cooldown")
    produced: List["ShipRefineShipRefine200ResponseDataProducedItem"] = Field(
        alias="produced"
    )
    consumed: List["ShipRefineShipRefine200ResponseDataConsumedItem"] = Field(
        alias="consumed"
    )
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
