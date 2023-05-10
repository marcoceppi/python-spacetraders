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
    from ..models.extraction_yield import ExtractionYield


T = TypeVar("T", bound="Extraction")


@attr.s(auto_attribs=True)
class Extraction:
    """
    Attributes:
        ship_symbol (str):
        yield_ (ExtractionYield):
    """

    ship_symbol: str
    yield_: "ExtractionYield"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.extraction_yield import ExtractionYield

        ship_symbol = self.ship_symbol
        yield_ = self.yield_.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "shipSymbol": ship_symbol,
                "yield": yield_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.extraction_yield import ExtractionYield

        d = src_dict.copy()
        ship_symbol = d.pop("shipSymbol")

        yield_ = ExtractionYield.from_dict(d.pop("yield"))

        extraction = cls(
            ship_symbol=ship_symbol,
            yield_=yield_,
        )

        extraction.additional_properties = d
        return extraction

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
