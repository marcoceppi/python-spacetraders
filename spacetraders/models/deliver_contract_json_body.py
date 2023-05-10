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
)

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="DeliverContractJsonBody")


@attr.s(auto_attribs=True)
class DeliverContractJsonBody:
    """
    Attributes:
        ship_symbol (str):
        trade_symbol (str):
        units (int):
    """

    ship_symbol: str
    trade_symbol: str
    units: int
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ship_symbol = self.ship_symbol
        trade_symbol = self.trade_symbol
        units = self.units

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "shipSymbol": ship_symbol,
                "tradeSymbol": trade_symbol,
                "units": units,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        ship_symbol = d.pop("shipSymbol")

        trade_symbol = d.pop("tradeSymbol")

        units = d.pop("units")

        deliver_contract_json_body = cls(
            ship_symbol=ship_symbol,
            trade_symbol=trade_symbol,
            units=units,
        )

        deliver_contract_json_body.additional_properties = d
        return deliver_contract_json_body

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
