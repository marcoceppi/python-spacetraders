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

from ..models.ship_type import ShipType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ship_engine import ShipEngine
    from ..models.ship_frame import ShipFrame
    from ..models.ship_module import ShipModule
    from ..models.ship_mount import ShipMount
    from ..models.ship_reactor import ShipReactor


T = TypeVar("T", bound="ShipyardShip")


@attr.s(auto_attribs=True)
class ShipyardShip:
    """
    Attributes:
        name (str):
        description (str):
        purchase_price (int):
        frame (ShipFrame): The frame of the ship. The frame determines the number of modules and mounting points of the
            ship, as well as base fuel capacity. As the condition of the frame takes more wear, the ship will become more
            sluggish and less maneuverable.
        reactor (ShipReactor): The reactor of the ship. The reactor is responsible for powering the ship's systems and
            weapons.
        engine (ShipEngine): The engine determines how quickly a ship travels between waypoints.
        modules (List['ShipModule']):
        mounts (List['ShipMount']):
        type (Union[Unset, ShipType]):
    """

    name: str
    description: str
    purchase_price: int
    frame: "ShipFrame"
    reactor: "ShipReactor"
    engine: "ShipEngine"
    modules: List["ShipModule"]
    mounts: List["ShipMount"]
    type: Union[Unset, ShipType] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.ship_engine import ShipEngine
        from ..models.ship_frame import ShipFrame
        from ..models.ship_module import ShipModule
        from ..models.ship_mount import ShipMount
        from ..models.ship_reactor import ShipReactor

        name = self.name
        description = self.description
        purchase_price = self.purchase_price
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

        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "description": description,
                "purchasePrice": purchase_price,
                "frame": frame,
                "reactor": reactor,
                "engine": engine,
                "modules": modules,
                "mounts": mounts,
            }
        )
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.ship_engine import ShipEngine
        from ..models.ship_frame import ShipFrame
        from ..models.ship_module import ShipModule
        from ..models.ship_mount import ShipMount
        from ..models.ship_reactor import ShipReactor

        d = src_dict.copy()
        name = d.pop("name")

        description = d.pop("description")

        purchase_price = d.pop("purchasePrice")

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

        _type = d.pop("type", UNSET)
        type: Union[Unset, ShipType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = ShipType(_type)

        shipyard_ship = cls(
            name=name,
            description=description,
            purchase_price=purchase_price,
            frame=frame,
            reactor=reactor,
            engine=engine,
            modules=modules,
            mounts=mounts,
            type=type,
        )

        shipyard_ship.additional_properties = d
        return shipyard_ship

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
