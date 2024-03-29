from typing import (
    Any,
    Dict,
    List,
    TypeVar,
)

from pydantic import BaseModel, Field

from ..models.construction_material import ConstructionMaterial
from ..types import Unset

T = TypeVar("T", bound="Construction")


class Construction(BaseModel):
    """The construction details of a waypoint.

    Attributes:
        symbol (str): The symbol of the waypoint.
        materials (List['ConstructionMaterial']): The materials required to construct the waypoint.
        is_complete (bool): Whether the waypoint has been constructed.
    """

    symbol: str = Field(alias="symbol")
    materials: List["ConstructionMaterial"] = Field(alias="materials")
    is_complete: bool = Field(alias="isComplete")
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
