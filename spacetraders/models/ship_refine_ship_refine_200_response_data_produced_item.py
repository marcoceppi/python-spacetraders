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
)

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ShipRefineShipRefine200ResponseDataProducedItem")


@attr.s(auto_attribs=True)
class ShipRefineShipRefine200ResponseDataProducedItem:
    """
    Attributes:
        trade_symbol (Union[Unset, str]):
        units (Union[Unset, int]):
    """

    trade_symbol: Union[Unset, str] = UNSET
    units: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        trade_symbol = self.trade_symbol
        units = self.units

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if trade_symbol is not UNSET:
            field_dict["tradeSymbol"] = trade_symbol
        if units is not UNSET:
            field_dict["units"] = units

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        trade_symbol = d.pop("tradeSymbol", UNSET)

        units = d.pop("units", UNSET)

        ship_refine_ship_refine_200_response_data_produced_item = cls(
            trade_symbol=trade_symbol,
            units=units,
        )

        ship_refine_ship_refine_200_response_data_produced_item.additional_properties = (
            d
        )
        return ship_refine_ship_refine_200_response_data_produced_item

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
