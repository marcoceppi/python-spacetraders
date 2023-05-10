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

from ..models.ship_module_symbol import ShipModuleSymbol
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ship_requirements import ShipRequirements


T = TypeVar("T", bound="ShipModule")


@attr.s(auto_attribs=True)
class ShipModule:
    """A module can be installed in a ship and provides a set of capabilities such as storage space or quarters for crew.
    Module installations are permanent.

        Attributes:
            symbol (ShipModuleSymbol):
            name (str):
            requirements (ShipRequirements): The requirements for installation on a ship
            capacity (Union[Unset, int]):
            range_ (Union[Unset, int]):
            description (Union[Unset, str]):
    """

    symbol: ShipModuleSymbol
    name: str
    requirements: "ShipRequirements"
    capacity: Union[Unset, int] = UNSET
    range_: Union[Unset, int] = UNSET
    description: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.ship_requirements import ShipRequirements

        symbol = self.symbol.value

        name = self.name
        requirements = self.requirements.to_dict()

        capacity = self.capacity
        range_ = self.range_
        description = self.description

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "symbol": symbol,
                "name": name,
                "requirements": requirements,
            }
        )
        if capacity is not UNSET:
            field_dict["capacity"] = capacity
        if range_ is not UNSET:
            field_dict["range"] = range_
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.ship_requirements import ShipRequirements

        d = src_dict.copy()
        symbol = ShipModuleSymbol(d.pop("symbol"))

        name = d.pop("name")

        requirements = ShipRequirements.from_dict(d.pop("requirements"))

        capacity = d.pop("capacity", UNSET)

        range_ = d.pop("range", UNSET)

        description = d.pop("description", UNSET)

        ship_module = cls(
            symbol=symbol,
            name=name,
            requirements=requirements,
            capacity=capacity,
            range_=range_,
            description=description,
        )

        ship_module.additional_properties = d
        return ship_module

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
