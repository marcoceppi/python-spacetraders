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
    from ..models.market_trade_good import MarketTradeGood
    from ..models.market_transaction import MarketTransaction
    from ..models.trade_good import TradeGood


T = TypeVar("T", bound="Market")


@attr.s(auto_attribs=True)
class Market:
    """
    Attributes:
        symbol (str): The symbol of the market. The symbol is the same as the waypoint where the market is located.
        exports (List['TradeGood']): The list of goods that are exported from this market.
        imports (List['TradeGood']): The list of goods that are sought as imports in this market.
        exchange (List['TradeGood']): The list of goods that are bought and sold between agents at this market.
        transactions (Union[Unset, List['MarketTransaction']]): The list of recent transactions at this market. Visible
            only when a ship is present at the market.
        trade_goods (Union[Unset, List['MarketTradeGood']]): The list of goods that are traded at this market. Visible
            only when a ship is present at the market.
    """

    symbol: str
    exports: List["TradeGood"]
    imports: List["TradeGood"]
    exchange: List["TradeGood"]
    transactions: Union[Unset, List["MarketTransaction"]] = UNSET
    trade_goods: Union[Unset, List["MarketTradeGood"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.market_trade_good import MarketTradeGood
        from ..models.market_transaction import MarketTransaction
        from ..models.trade_good import TradeGood

        symbol = self.symbol
        exports = []
        for exports_item_data in self.exports:
            exports_item = exports_item_data.to_dict()

            exports.append(exports_item)

        imports = []
        for imports_item_data in self.imports:
            imports_item = imports_item_data.to_dict()

            imports.append(imports_item)

        exchange = []
        for exchange_item_data in self.exchange:
            exchange_item = exchange_item_data.to_dict()

            exchange.append(exchange_item)

        transactions: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.transactions, Unset):
            transactions = []
            for transactions_item_data in self.transactions:
                transactions_item = transactions_item_data.to_dict()

                transactions.append(transactions_item)

        trade_goods: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.trade_goods, Unset):
            trade_goods = []
            for trade_goods_item_data in self.trade_goods:
                trade_goods_item = trade_goods_item_data.to_dict()

                trade_goods.append(trade_goods_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "symbol": symbol,
                "exports": exports,
                "imports": imports,
                "exchange": exchange,
            }
        )
        if transactions is not UNSET:
            field_dict["transactions"] = transactions
        if trade_goods is not UNSET:
            field_dict["tradeGoods"] = trade_goods

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.market_trade_good import MarketTradeGood
        from ..models.market_transaction import MarketTransaction
        from ..models.trade_good import TradeGood

        d = src_dict.copy()
        symbol = d.pop("symbol")

        exports = []
        _exports = d.pop("exports")
        for exports_item_data in _exports:
            exports_item = TradeGood.from_dict(exports_item_data)

            exports.append(exports_item)

        imports = []
        _imports = d.pop("imports")
        for imports_item_data in _imports:
            imports_item = TradeGood.from_dict(imports_item_data)

            imports.append(imports_item)

        exchange = []
        _exchange = d.pop("exchange")
        for exchange_item_data in _exchange:
            exchange_item = TradeGood.from_dict(exchange_item_data)

            exchange.append(exchange_item)

        transactions = []
        _transactions = d.pop("transactions", UNSET)
        for transactions_item_data in _transactions or []:
            transactions_item = MarketTransaction.from_dict(transactions_item_data)

            transactions.append(transactions_item)

        trade_goods = []
        _trade_goods = d.pop("tradeGoods", UNSET)
        for trade_goods_item_data in _trade_goods or []:
            trade_goods_item = MarketTradeGood.from_dict(trade_goods_item_data)

            trade_goods.append(trade_goods_item)

        market = cls(
            symbol=symbol,
            exports=exports,
            imports=imports,
            exchange=exchange,
            transactions=transactions,
            trade_goods=trade_goods,
        )

        market.additional_properties = d
        return market

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
