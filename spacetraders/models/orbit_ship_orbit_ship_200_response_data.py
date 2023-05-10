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
    from ..models.ship_nav import ShipNav


T = TypeVar("T", bound="OrbitShipOrbitShip200ResponseData")


@attr.s(auto_attribs=True)
class OrbitShipOrbitShip200ResponseData:
    """
    Attributes:
        nav (ShipNav): The navigation information of the ship.
    """

    nav: "ShipNav"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.ship_nav import ShipNav

        nav = self.nav.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "nav": nav,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.ship_nav import ShipNav

        d = src_dict.copy()
        nav = ShipNav.from_dict(d.pop("nav"))

        orbit_ship_orbit_ship_200_response_data = cls(
            nav=nav,
        )

        orbit_ship_orbit_ship_200_response_data.additional_properties = d
        return orbit_ship_orbit_ship_200_response_data

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
