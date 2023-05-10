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
    from ..models.ship_fuel import ShipFuel
    from ..models.ship_nav import ShipNav


T = TypeVar("T", bound="WarpShipResponse200Data")


@attr.s(auto_attribs=True)
class WarpShipResponse200Data:
    """
    Attributes:
        fuel (ShipFuel): Details of the ship's fuel tanks including how much fuel was consumed during the last transit
            or action.
        nav (ShipNav): The navigation information of the ship.
    """

    fuel: "ShipFuel"
    nav: "ShipNav"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.ship_fuel import ShipFuel
        from ..models.ship_nav import ShipNav

        fuel = self.fuel.to_dict()

        nav = self.nav.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "fuel": fuel,
                "nav": nav,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.ship_fuel import ShipFuel
        from ..models.ship_nav import ShipNav

        d = src_dict.copy()
        fuel = ShipFuel.from_dict(d.pop("fuel"))

        nav = ShipNav.from_dict(d.pop("nav"))

        warp_ship_response_200_data = cls(
            fuel=fuel,
            nav=nav,
        )

        warp_ship_response_200_data.additional_properties = d
        return warp_ship_response_200_data

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
