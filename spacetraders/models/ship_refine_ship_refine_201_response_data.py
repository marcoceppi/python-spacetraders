from typing import (
    Any,
    Dict,
    List,
    TypeVar,
)

from pydantic import BaseModel, Field

from ..models.cooldown import Cooldown
from ..models.ship_cargo import ShipCargo
from ..models.ship_refine_ship_refine_201_response_data_consumed_item import (
    ShipRefineShipRefine201ResponseDataConsumedItem,
)
from ..models.ship_refine_ship_refine_201_response_data_produced_item import (
    ShipRefineShipRefine201ResponseDataProducedItem,
)
from ..types import Unset

T = TypeVar("T", bound="ShipRefineShipRefine201ResponseData")


class ShipRefineShipRefine201ResponseData(BaseModel):
    """
    Attributes:
        cargo (ShipCargo): Ship cargo details.
        cooldown (Cooldown): A cooldown is a period of time in which a ship cannot perform certain actions.
        produced (List['ShipRefineShipRefine201ResponseDataProducedItem']): Goods that were produced by this refining
            process.
        consumed (List['ShipRefineShipRefine201ResponseDataConsumedItem']): Goods that were consumed during this
            refining process.
    """

    cargo: "ShipCargo" = Field(alias="cargo")
    cooldown: "Cooldown" = Field(alias="cooldown")
    produced: List["ShipRefineShipRefine201ResponseDataProducedItem"] = Field(
        alias="produced"
    )
    consumed: List["ShipRefineShipRefine201ResponseDataConsumedItem"] = Field(
        alias="consumed"
    )
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
