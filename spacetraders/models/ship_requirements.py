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

from ..types import UNSET, Unset

T = TypeVar("T", bound="ShipRequirements")


@attr.s(auto_attribs=True)
class ShipRequirements:
    """The requirements for installation on a ship

    Attributes:
        power (Union[Unset, int]): The amount of power required from the reactor.
        crew (Union[Unset, int]): The number of crew required for operation.
        slots (Union[Unset, int]): The number of module slots required for installation.
    """

    power: Union[Unset, int] = UNSET
    crew: Union[Unset, int] = UNSET
    slots: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        power = self.power
        crew = self.crew
        slots = self.slots

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if power is not UNSET:
            field_dict["power"] = power
        if crew is not UNSET:
            field_dict["crew"] = crew
        if slots is not UNSET:
            field_dict["slots"] = slots

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        power = d.pop("power", UNSET)

        crew = d.pop("crew", UNSET)

        slots = d.pop("slots", UNSET)

        ship_requirements = cls(
            power=power,
            crew=crew,
            slots=slots,
        )

        ship_requirements.additional_properties = d
        return ship_requirements

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
