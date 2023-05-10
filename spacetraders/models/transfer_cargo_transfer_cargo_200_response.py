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
    from ..models.transfer_cargo_transfer_cargo_200_response_data import (
        TransferCargoTransferCargo200ResponseData,
    )


T = TypeVar("T", bound="TransferCargoTransferCargo200Response")


@attr.s(auto_attribs=True)
class TransferCargoTransferCargo200Response:
    """
    Attributes:
        data (TransferCargoTransferCargo200ResponseData):
    """

    data: "TransferCargoTransferCargo200ResponseData"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.transfer_cargo_transfer_cargo_200_response_data import (
            TransferCargoTransferCargo200ResponseData,
        )

        data = self.data.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data": data,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.transfer_cargo_transfer_cargo_200_response_data import (
            TransferCargoTransferCargo200ResponseData,
        )

        d = src_dict.copy()
        data = TransferCargoTransferCargo200ResponseData.from_dict(d.pop("data"))

        transfer_cargo_transfer_cargo_200_response = cls(
            data=data,
        )

        transfer_cargo_transfer_cargo_200_response.additional_properties = d
        return transfer_cargo_transfer_cargo_200_response

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
