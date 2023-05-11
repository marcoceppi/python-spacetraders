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
    Union,
)

import attr
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

    power: Union[Unset, int] = UNSET
    crew: Union[Unset, int] = UNSET
    slots: Union[Unset, int] = UNSET
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
