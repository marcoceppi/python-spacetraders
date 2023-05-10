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
    from ..models.shipyard_ship import ShipyardShip
    from ..models.shipyard_ship_types_item import ShipyardShipTypesItem
    from ..models.shipyard_transaction import ShipyardTransaction


T = TypeVar("T", bound="Shipyard")


@attr.s(auto_attribs=True)
class Shipyard:
    """
    Attributes:
        symbol (str): The symbol of the shipyard. The symbol is the same as the waypoint where the shipyard is located.
        ship_types (List['ShipyardShipTypesItem']): The list of ship types available for purchase at this shipyard.
        transactions (Union[Unset, List['ShipyardTransaction']]): The list of recent transactions at this shipyard.
        ships (Union[Unset, List['ShipyardShip']]): The ships that are currently available for purchase at the shipyard.
    """

    symbol: str
    ship_types: List["ShipyardShipTypesItem"]
    transactions: Union[Unset, List["ShipyardTransaction"]] = UNSET
    ships: Union[Unset, List["ShipyardShip"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.shipyard_ship import ShipyardShip
        from ..models.shipyard_ship_types_item import ShipyardShipTypesItem
        from ..models.shipyard_transaction import ShipyardTransaction

        symbol = self.symbol
        ship_types = []
        for ship_types_item_data in self.ship_types:
            ship_types_item = ship_types_item_data.to_dict()

            ship_types.append(ship_types_item)

        transactions: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.transactions, Unset):
            transactions = []
            for transactions_item_data in self.transactions:
                transactions_item = transactions_item_data.to_dict()

                transactions.append(transactions_item)

        ships: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.ships, Unset):
            ships = []
            for ships_item_data in self.ships:
                ships_item = ships_item_data.to_dict()

                ships.append(ships_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "symbol": symbol,
                "shipTypes": ship_types,
            }
        )
        if transactions is not UNSET:
            field_dict["transactions"] = transactions
        if ships is not UNSET:
            field_dict["ships"] = ships

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.shipyard_ship import ShipyardShip
        from ..models.shipyard_ship_types_item import ShipyardShipTypesItem
        from ..models.shipyard_transaction import ShipyardTransaction

        d = src_dict.copy()
        symbol = d.pop("symbol")

        ship_types = []
        _ship_types = d.pop("shipTypes")
        for ship_types_item_data in _ship_types:
            ship_types_item = ShipyardShipTypesItem.from_dict(ship_types_item_data)

            ship_types.append(ship_types_item)

        transactions = []
        _transactions = d.pop("transactions", UNSET)
        for transactions_item_data in _transactions or []:
            transactions_item = ShipyardTransaction.from_dict(transactions_item_data)

            transactions.append(transactions_item)

        ships = []
        _ships = d.pop("ships", UNSET)
        for ships_item_data in _ships or []:
            ships_item = ShipyardShip.from_dict(ships_item_data)

            ships.append(ships_item)

        shipyard = cls(
            symbol=symbol,
            ship_types=ship_types,
            transactions=transactions,
            ships=ships,
        )

        shipyard.additional_properties = d
        return shipyard

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
