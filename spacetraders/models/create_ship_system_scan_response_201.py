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
from pydantic import BaseModel, Field

from ..models.create_ship_system_scan_response_201_data import (
    CreateShipSystemScanResponse201Data,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateShipSystemScanResponse201")


class CreateShipSystemScanResponse201(BaseModel):
    """
    Attributes:
        data (CreateShipSystemScanResponse201Data):
    """

    data: "CreateShipSystemScanResponse201Data" = Field(alias="data")
    additional_properties: Dict[str, Any] = {}

    class Config:
        arbitrary_types_allowed = True

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
