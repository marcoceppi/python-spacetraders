from typing import (
    Any,
    Dict,
    List,
    TypeVar,
    Union,
)

from pydantic import BaseModel, Field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ShipRequirements")


class ShipRequirements(BaseModel):
    """The requirements for installation on a ship

    Attributes:
        power (Union[Unset, int]): The amount of power required from the reactor.
        crew (Union[Unset, int]): The number of crew required for operation.
        slots (Union[Unset, int]): The number of module slots required for installation.
    """

    power: Union[Unset, int] = Field(UNSET, alias="power")
    crew: Union[Unset, int] = Field(UNSET, alias="crew")
    slots: Union[Unset, int] = Field(UNSET, alias="slots")
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
