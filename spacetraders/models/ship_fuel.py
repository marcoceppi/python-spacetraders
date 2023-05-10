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
    cast,
)

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ship_fuel_consumed import ShipFuelConsumed


T = TypeVar("T", bound="ShipFuel")


@attr.s(auto_attribs=True)
class ShipFuel:
    """Details of the ship's fuel tanks including how much fuel was consumed during the last transit or action.

    Attributes:
        current (int): The current amount of fuel in the ship's tanks.
        capacity (int): The maximum amount of fuel the ship's tanks can hold.
        consumed (Union[Unset, ShipFuelConsumed]):
    """

    current: int
    capacity: int
    consumed: Union[Unset, "ShipFuelConsumed"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.ship_fuel_consumed import ShipFuelConsumed

        current = self.current
        capacity = self.capacity
        consumed: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.consumed, Unset):
            consumed = self.consumed.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "current": current,
                "capacity": capacity,
            }
        )
        if consumed is not UNSET:
            field_dict["consumed"] = consumed

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.ship_fuel_consumed import ShipFuelConsumed

        d = src_dict.copy()
        current = d.pop("current")

        capacity = d.pop("capacity")

        _consumed = d.pop("consumed", UNSET)
        consumed: Union[Unset, ShipFuelConsumed]
        if isinstance(_consumed, Unset):
            consumed = UNSET
        else:
            consumed = ShipFuelConsumed.from_dict(_consumed)

        ship_fuel = cls(
            current=current,
            capacity=capacity,
            consumed=consumed,
        )

        ship_fuel.additional_properties = d
        return ship_fuel

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
