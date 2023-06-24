from typing import (
    Any,
    Dict,
    List,
    TypeVar,
)

from pydantic import BaseModel, Field

from ..types import Unset

T = TypeVar("T", bound="Meta")


class Meta(BaseModel):
    """Meta details for pagination.

    Attributes:
        total (int): Shows the total amount of items of this kind that exist.
        page (int): A page denotes an amount of items, offset from the first item. Each page holds an amount of items
            equal to the `limit`. Default: 1.
        limit (int): The amount of items in each page. Limits how many items can be fetched at once. Default: 10.
    """

    total: int = Field(alias="total")
    page: int = Field(1, alias="page")
    limit: int = Field(10, alias="limit")
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
