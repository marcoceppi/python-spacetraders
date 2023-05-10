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
    from ..models.cooldown import Cooldown
    from ..models.ship_nav import ShipNav


T = TypeVar("T", bound="JumpShipResponse200Data")


@attr.s(auto_attribs=True)
class JumpShipResponse200Data:
    """
    Attributes:
        cooldown (Cooldown): A cooldown is a period of time in which a ship cannot perform certain actions.
        nav (Union[Unset, ShipNav]): The navigation information of the ship.
    """

    cooldown: "Cooldown"
    nav: Union[Unset, "ShipNav"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.cooldown import Cooldown
        from ..models.ship_nav import ShipNav

        cooldown = self.cooldown.to_dict()

        nav: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.nav, Unset):
            nav = self.nav.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "cooldown": cooldown,
            }
        )
        if nav is not UNSET:
            field_dict["nav"] = nav

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.cooldown import Cooldown
        from ..models.ship_nav import ShipNav

        d = src_dict.copy()
        cooldown = Cooldown.from_dict(d.pop("cooldown"))

        _nav = d.pop("nav", UNSET)
        nav: Union[Unset, ShipNav]
        if isinstance(_nav, Unset):
            nav = UNSET
        else:
            nav = ShipNav.from_dict(_nav)

        jump_ship_response_200_data = cls(
            cooldown=cooldown,
            nav=nav,
        )

        jump_ship_response_200_data.additional_properties = d
        return jump_ship_response_200_data

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
