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

from ..models.ship_reactor_symbol import ShipReactorSymbol
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ship_requirements import ShipRequirements


T = TypeVar("T", bound="ShipReactor")


@attr.s(auto_attribs=True)
class ShipReactor:
    """The reactor of the ship. The reactor is responsible for powering the ship's systems and weapons.

    Attributes:
        symbol (ShipReactorSymbol):
        name (str):
        description (str):
        power_output (int):
        requirements (ShipRequirements): The requirements for installation on a ship
        condition (Union[Unset, int]): Condition is a range of 0 to 100 where 0 is completely worn out and 100 is brand
            new.
    """

    symbol: ShipReactorSymbol
    name: str
    description: str
    power_output: int
    requirements: "ShipRequirements"
    condition: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.ship_requirements import ShipRequirements

        symbol = self.symbol.value

        name = self.name
        description = self.description
        power_output = self.power_output
        requirements = self.requirements.to_dict()

        condition = self.condition

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "symbol": symbol,
                "name": name,
                "description": description,
                "powerOutput": power_output,
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
        symbol = ShipReactorSymbol(d.pop("symbol"))

        name = d.pop("name")

        description = d.pop("description")

        power_output = d.pop("powerOutput")

        requirements = ShipRequirements.from_dict(d.pop("requirements"))

        condition = d.pop("condition", UNSET)

        ship_reactor = cls(
            symbol=symbol,
            name=name,
            description=description,
            power_output=power_output,
            requirements=requirements,
            condition=condition,
        )

        ship_reactor.additional_properties = d
        return ship_reactor

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
