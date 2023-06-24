from typing import (
    Any,
    Dict,
    List,
    TypeVar,
    Union,
)

from pydantic import BaseModel, Field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RefuelShipJsonBody")


class RefuelShipJsonBody(BaseModel):
    """
    Attributes:
        units (Union[Unset, int]): The amount of fuel to fill in the ship's tanks. When not specified, the ship will be
            refueled to its maximum fuel capacity. If the amount specified is greater than the ship's remaining capacity,
            the ship will only be refueled to its maximum fuel capacity. The amount specified is not in market units but in
            ship fuel units. Example: 100.
    """

    units: Union[Unset, int] = Field(UNSET, alias="units")
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
