from typing import (
    Any,
    Dict,
    List,
    TypeVar,
)

from pydantic import BaseModel, Field

from ..models.faction import Faction
from ..models.meta import Meta
from ..types import Unset

T = TypeVar("T", bound="GetFactionsResponse200")


class GetFactionsResponse200(BaseModel):
    """
    Attributes:
        data (List['Faction']):
        meta (Meta): Meta details for pagination.
    """

    data: List["Faction"] = Field(alias="data")
    meta: "Meta" = Field(alias="meta")
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
