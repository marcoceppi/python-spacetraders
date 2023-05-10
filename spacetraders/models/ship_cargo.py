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

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ship_cargo_item import ShipCargoItem


T = TypeVar("T", bound="ShipCargo")


@attr.s(auto_attribs=True)
class ShipCargo:
    """
    Attributes:
        capacity (int): The max number of items that can be stored in the cargo hold.
        units (int): The number of items currently stored in the cargo hold.
        inventory (List['ShipCargoItem']): The items currently in the cargo hold.
    """

    capacity: int
    units: int
    inventory: List["ShipCargoItem"]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.ship_cargo_item import ShipCargoItem

        capacity = self.capacity
        units = self.units
        inventory = []
        for inventory_item_data in self.inventory:
            inventory_item = inventory_item_data.to_dict()

            inventory.append(inventory_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "capacity": capacity,
                "units": units,
                "inventory": inventory,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.ship_cargo_item import ShipCargoItem

        d = src_dict.copy()
        capacity = d.pop("capacity")

        units = d.pop("units")

        inventory = []
        _inventory = d.pop("inventory")
        for inventory_item_data in _inventory:
            inventory_item = ShipCargoItem.from_dict(inventory_item_data)

            inventory.append(inventory_item)

        ship_cargo = cls(
            capacity=capacity,
            units=units,
            inventory=inventory,
        )

        ship_cargo.additional_properties = d
        return ship_cargo

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
