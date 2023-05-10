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
    from ..models.extract_resources_response_201_data import (
        ExtractResourcesResponse201Data,
    )


T = TypeVar("T", bound="ExtractResourcesResponse201")


@attr.s(auto_attribs=True)
class ExtractResourcesResponse201:
    """
    Attributes:
        data (ExtractResourcesResponse201Data):
    """

    data: "ExtractResourcesResponse201Data"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.extract_resources_response_201_data import (
            ExtractResourcesResponse201Data,
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
        from ..models.extract_resources_response_201_data import (
            ExtractResourcesResponse201Data,
        )

        d = src_dict.copy()
        data = ExtractResourcesResponse201Data.from_dict(d.pop("data"))

        extract_resources_response_201 = cls(
            data=data,
        )

        extract_resources_response_201.additional_properties = d
        return extract_resources_response_201

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
