from typing import (
    Any,
    Dict,
    List,
    TypeVar,
    Union,
)

from pydantic import BaseModel, Field

from ..models.shipyard_ship import ShipyardShip
from ..models.shipyard_ship_types_item import ShipyardShipTypesItem
from ..models.shipyard_transaction import ShipyardTransaction
from ..types import UNSET, Unset

T = TypeVar("T", bound="Shipyard")


class Shipyard(BaseModel):
    """
    Attributes:
        symbol (str): The symbol of the shipyard. The symbol is the same as the waypoint where the shipyard is located.
        ship_types (List['ShipyardShipTypesItem']): The list of ship types available for purchase at this shipyard.
        modifications_fee (int): The fee to modify a ship at this shipyard. This includes installing or removing modules
            and mounts on a ship. In the case of mounts, the fee is a flat rate per mount. In the case of modules, the fee
            is per slot the module occupies.
        transactions (Union[Unset, List['ShipyardTransaction']]): The list of recent transactions at this shipyard.
        ships (Union[Unset, List['ShipyardShip']]): The ships that are currently available for purchase at the shipyard.
    """

    symbol: str = Field(alias="symbol")
    ship_types: List["ShipyardShipTypesItem"] = Field(alias="shipTypes")
    modifications_fee: int = Field(alias="modificationsFee")
    transactions: Union[Unset, List["ShipyardTransaction"]] = Field(
        UNSET, alias="transactions"
    )
    ships: Union[Unset, List["ShipyardShip"]] = Field(UNSET, alias="ships")
    additional_properties: Dict[str, Any] = {}

    class Config:
        arbitrary_types_allowed = True
        allow_population_by_field_name = True

    def dict(self, *args, **kwargs):
        output = super().dict(*args, **kwargs)
        return {k: v for k, v in output.items() if not isinstance(v, Unset)}

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
