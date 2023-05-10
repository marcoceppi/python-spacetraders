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

from ..models.ship_frame_symbol import ShipFrameSymbol
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ship_requirements import ShipRequirements


T = TypeVar("T", bound="ShipFrame")


@attr.s(auto_attribs=True)
class ShipFrame:
    """The frame of the ship. The frame determines the number of modules and mounting points of the ship, as well as base
    fuel capacity. As the condition of the frame takes more wear, the ship will become more sluggish and less
    maneuverable.

        Attributes:
            symbol (ShipFrameSymbol):
            name (str):
            description (str):
            module_slots (int):
            mounting_points (int):
            fuel_capacity (int):
            requirements (ShipRequirements): The requirements for installation on a ship
            condition (Union[Unset, int]): Condition is a range of 0 to 100 where 0 is completely worn out and 100 is brand
                new.
    """

    symbol: ShipFrameSymbol
    name: str
    description: str
    module_slots: int
    mounting_points: int
    fuel_capacity: int
    requirements: "ShipRequirements"
    condition: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.ship_requirements import ShipRequirements

        symbol = self.symbol.value

        name = self.name
        description = self.description
        module_slots = self.module_slots
        mounting_points = self.mounting_points
        fuel_capacity = self.fuel_capacity
        requirements = self.requirements.to_dict()

        condition = self.condition

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "symbol": symbol,
                "name": name,
                "description": description,
                "moduleSlots": module_slots,
                "mountingPoints": mounting_points,
                "fuelCapacity": fuel_capacity,
                "requirements": requirements,
            }
        )
        if condition is not UNSET:
            field_dict["condition"] = condition

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.ship_requirements import ShipRequirements

        d = src_dict.copy()
        symbol = ShipFrameSymbol(d.pop("symbol"))

        name = d.pop("name")

        description = d.pop("description")

        module_slots = d.pop("moduleSlots")

        mounting_points = d.pop("mountingPoints")

        fuel_capacity = d.pop("fuelCapacity")

        requirements = ShipRequirements.from_dict(d.pop("requirements"))

        condition = d.pop("condition", UNSET)

        ship_frame = cls(
            symbol=symbol,
            name=name,
            description=description,
            module_slots=module_slots,
            mounting_points=mounting_points,
            fuel_capacity=fuel_capacity,
            requirements=requirements,
            condition=condition,
        )

        ship_frame.additional_properties = d
        return ship_frame

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
