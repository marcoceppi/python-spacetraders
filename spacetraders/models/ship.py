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
    from ..models.ship_cargo import ShipCargo
    from ..models.ship_crew import ShipCrew
    from ..models.ship_engine import ShipEngine
    from ..models.ship_frame import ShipFrame
    from ..models.ship_fuel import ShipFuel
    from ..models.ship_module import ShipModule
    from ..models.ship_mount import ShipMount
    from ..models.ship_nav import ShipNav
    from ..models.ship_reactor import ShipReactor
    from ..models.ship_registration import ShipRegistration


T = TypeVar("T", bound="Ship")


@attr.s(auto_attribs=True)
class Ship:
    """A ship

    Attributes:
        symbol (str): The globally unique identifier of the ship in the following format: `[AGENT_SYMBOL]_[HEX_ID]`
        registration (ShipRegistration): The public registration information of the ship
        nav (ShipNav): The navigation information of the ship.
        crew (ShipCrew): The ship's crew service and maintain the ship's systems and equipment.
        frame (ShipFrame): The frame of the ship. The frame determines the number of modules and mounting points of the
            ship, as well as base fuel capacity. As the condition of the frame takes more wear, the ship will become more
            sluggish and less maneuverable.
        reactor (ShipReactor): The reactor of the ship. The reactor is responsible for powering the ship's systems and
            weapons.
        engine (ShipEngine): The engine determines how quickly a ship travels between waypoints.
        modules (List['ShipModule']):
        mounts (List['ShipMount']):
        cargo (ShipCargo):
        fuel (ShipFuel): Details of the ship's fuel tanks including how much fuel was consumed during the last transit
            or action.
    """

    symbol: str
    registration: "ShipRegistration"
    nav: "ShipNav"
    crew: "ShipCrew"
    frame: "ShipFrame"
    reactor: "ShipReactor"
    engine: "ShipEngine"
    modules: List["ShipModule"]
    mounts: List["ShipMount"]
    cargo: "ShipCargo"
    fuel: "ShipFuel"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.ship_cargo import ShipCargo
        from ..models.ship_crew import ShipCrew
        from ..models.ship_engine import ShipEngine
        from ..models.ship_frame import ShipFrame
        from ..models.ship_fuel import ShipFuel
        from ..models.ship_module import ShipModule
        from ..models.ship_mount import ShipMount
        from ..models.ship_nav import ShipNav
        from ..models.ship_reactor import ShipReactor
        from ..models.ship_registration import ShipRegistration

        symbol = self.symbol
        registration = self.registration.to_dict()

        nav = self.nav.to_dict()

        crew = self.crew.to_dict()

        frame = self.frame.to_dict()

        reactor = self.reactor.to_dict()

        engine = self.engine.to_dict()

        modules = []
        for modules_item_data in self.modules:
            modules_item = modules_item_data.to_dict()

            modules.append(modules_item)

        mounts = []
        for mounts_item_data in self.mounts:
            mounts_item = mounts_item_data.to_dict()

            mounts.append(mounts_item)

        cargo = self.cargo.to_dict()

        fuel = self.fuel.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "symbol": symbol,
                "registration": registration,
                "nav": nav,
                "crew": crew,
                "frame": frame,
                "reactor": reactor,
                "engine": engine,
                "modules": modules,
                "mounts": mounts,
                "cargo": cargo,
                "fuel": fuel,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.ship_cargo import ShipCargo
        from ..models.ship_crew import ShipCrew
        from ..models.ship_engine import ShipEngine
        from ..models.ship_frame import ShipFrame
        from ..models.ship_fuel import ShipFuel
        from ..models.ship_module import ShipModule
        from ..models.ship_mount import ShipMount
        from ..models.ship_nav import ShipNav
        from ..models.ship_reactor import ShipReactor
        from ..models.ship_registration import ShipRegistration

        d = src_dict.copy()
        symbol = d.pop("symbol")

        registration = ShipRegistration.from_dict(d.pop("registration"))

        nav = ShipNav.from_dict(d.pop("nav"))

        crew = ShipCrew.from_dict(d.pop("crew"))

        frame = ShipFrame.from_dict(d.pop("frame"))

        reactor = ShipReactor.from_dict(d.pop("reactor"))

        engine = ShipEngine.from_dict(d.pop("engine"))

        modules = []
        _modules = d.pop("modules")
        for modules_item_data in _modules:
            modules_item = ShipModule.from_dict(modules_item_data)

            modules.append(modules_item)

        mounts = []
        _mounts = d.pop("mounts")
        for mounts_item_data in _mounts:
            mounts_item = ShipMount.from_dict(mounts_item_data)

            mounts.append(mounts_item)

        cargo = ShipCargo.from_dict(d.pop("cargo"))

        fuel = ShipFuel.from_dict(d.pop("fuel"))

        ship = cls(
            symbol=symbol,
            registration=registration,
            nav=nav,
            crew=crew,
            frame=frame,
            reactor=reactor,
            engine=engine,
            modules=modules,
            mounts=mounts,
            cargo=cargo,
            fuel=fuel,
        )

        ship.additional_properties = d
        return ship

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
