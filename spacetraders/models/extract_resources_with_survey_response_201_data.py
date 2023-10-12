from typing import (
    Any,
    Dict,
    List,
    TypeVar,
)

from pydantic import BaseModel, Field

from ..models.cooldown import Cooldown
from ..models.extraction import Extraction
from ..models.ship_cargo import ShipCargo
from ..types import Unset

T = TypeVar("T", bound="ExtractResourcesWithSurveyResponse201Data")


class ExtractResourcesWithSurveyResponse201Data(BaseModel):
    """
    Attributes:
        cooldown (Cooldown): A cooldown is a period of time in which a ship cannot perform certain actions.
        extraction (Extraction): Extraction details.
        cargo (ShipCargo): Ship cargo details.
    """

    cooldown: "Cooldown" = Field(alias="cooldown")
    extraction: "Extraction" = Field(alias="extraction")
    cargo: "ShipCargo" = Field(alias="cargo")
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
