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
    from ..models.scanned_ship_engine import ScannedShipEngine
    from ..models.scanned_ship_frame import ScannedShipFrame
    from ..models.scanned_ship_mounts_item import ScannedShipMountsItem
    from ..models.scanned_ship_reactor import ScannedShipReactor
    from ..models.ship_nav import ShipNav
    from ..models.ship_registration import ShipRegistration


T = TypeVar("T", bound="ScannedShip")


@attr.s(auto_attribs=True)
class ScannedShip:
    """The ship that was scanned. Details include information about the ship that could be detected by the scanner.

    Attributes:
        symbol (str): The globally unique identifier of the ship.
        registration (ShipRegistration): The public registration information of the ship
        nav (ShipNav): The navigation information of the ship.
        engine (ScannedShipEngine): The engine of the ship.
        frame (Union[Unset, ScannedShipFrame]): The frame of the ship.
        reactor (Union[Unset, ScannedShipReactor]): The reactor of the ship.
        mounts (Union[Unset, List['ScannedShipMountsItem']]):
    """

    symbol: str
    registration: "ShipRegistration"
    nav: "ShipNav"
    engine: "ScannedShipEngine"
    frame: Union[Unset, "ScannedShipFrame"] = UNSET
    reactor: Union[Unset, "ScannedShipReactor"] = UNSET
    mounts: Union[Unset, List["ScannedShipMountsItem"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.scanned_ship_engine import ScannedShipEngine
        from ..models.scanned_ship_frame import ScannedShipFrame
        from ..models.scanned_ship_mounts_item import ScannedShipMountsItem
        from ..models.scanned_ship_reactor import ScannedShipReactor
        from ..models.ship_nav import ShipNav
        from ..models.ship_registration import ShipRegistration

        symbol = self.symbol
        registration = self.registration.to_dict()

        nav = self.nav.to_dict()

        engine = self.engine.to_dict()

        frame: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.frame, Unset):
            frame = self.frame.to_dict()

        reactor: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.reactor, Unset):
            reactor = self.reactor.to_dict()

        mounts: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.mounts, Unset):
            mounts = []
            for mounts_item_data in self.mounts:
                mounts_item = mounts_item_data.to_dict()

                mounts.append(mounts_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "symbol": symbol,
                "registration": registration,
                "nav": nav,
                "engine": engine,
            }
        )
        if frame is not UNSET:
            field_dict["frame"] = frame
        if reactor is not UNSET:
            field_dict["reactor"] = reactor
        if mounts is not UNSET:
            field_dict["mounts"] = mounts

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.scanned_ship_engine import ScannedShipEngine
        from ..models.scanned_ship_frame import ScannedShipFrame
        from ..models.scanned_ship_mounts_item import ScannedShipMountsItem
        from ..models.scanned_ship_reactor import ScannedShipReactor
        from ..models.ship_nav import ShipNav
        from ..models.ship_registration import ShipRegistration

        d = src_dict.copy()
        symbol = d.pop("symbol")

        registration = ShipRegistration.from_dict(d.pop("registration"))

        nav = ShipNav.from_dict(d.pop("nav"))

        engine = ScannedShipEngine.from_dict(d.pop("engine"))

        _frame = d.pop("frame", UNSET)
        frame: Union[Unset, ScannedShipFrame]
        if isinstance(_frame, Unset):
            frame = UNSET
        else:
            frame = ScannedShipFrame.from_dict(_frame)

        _reactor = d.pop("reactor", UNSET)
        reactor: Union[Unset, ScannedShipReactor]
        if isinstance(_reactor, Unset):
            reactor = UNSET
        else:
            reactor = ScannedShipReactor.from_dict(_reactor)

        mounts = []
        _mounts = d.pop("mounts", UNSET)
        for mounts_item_data in _mounts or []:
            mounts_item = ScannedShipMountsItem.from_dict(mounts_item_data)

            mounts.append(mounts_item)

        scanned_ship = cls(
            symbol=symbol,
            registration=registration,
            nav=nav,
            engine=engine,
            frame=frame,
            reactor=reactor,
            mounts=mounts,
        )

        scanned_ship.additional_properties = d
        return scanned_ship

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
