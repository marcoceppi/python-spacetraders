import datetime
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
from dateutil.parser import isoparse

from ..models.survey_size import SurveySize
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.survey_deposit import SurveyDeposit


T = TypeVar("T", bound="Survey")


@attr.s(auto_attribs=True)
class Survey:
    """A resource survey of a waypoint, detailing a specific extraction location and the types of resources that can be
    found there.

        Attributes:
            signature (str): A unique signature for the location of this survey. This signature is verified when attempting
                an extraction using this survey.
            symbol (str): The symbol of the waypoint that this survey is for.
            deposits (List['SurveyDeposit']): A list of deposits that can be found at this location.
            expiration (datetime.datetime): The date and time when the survey expires. After this date and time, the survey
                will no longer be available for extraction.
            size (SurveySize): The size of the deposit. This value indicates how much can be extracted from the survey
                before it is exhausted.
    """

    signature: str
    symbol: str
    deposits: List["SurveyDeposit"]
    expiration: datetime.datetime
    size: SurveySize
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.survey_deposit import SurveyDeposit

        signature = self.signature
        symbol = self.symbol
        deposits = []
        for deposits_item_data in self.deposits:
            deposits_item = deposits_item_data.to_dict()

            deposits.append(deposits_item)

        expiration = self.expiration.isoformat()

        size = self.size.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "signature": signature,
                "symbol": symbol,
                "deposits": deposits,
                "expiration": expiration,
                "size": size,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.survey_deposit import SurveyDeposit

        d = src_dict.copy()
        signature = d.pop("signature")

        symbol = d.pop("symbol")

        deposits = []
        _deposits = d.pop("deposits")
        for deposits_item_data in _deposits:
            deposits_item = SurveyDeposit.from_dict(deposits_item_data)

            deposits.append(deposits_item)

        expiration = isoparse(d.pop("expiration"))

        size = SurveySize(d.pop("size"))

        survey = cls(
            signature=signature,
            symbol=symbol,
            deposits=deposits,
            expiration=expiration,
            size=size,
        )

        survey.additional_properties = d
        return survey

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
