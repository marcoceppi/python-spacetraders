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
    from ..models.survey import Survey


T = TypeVar("T", bound="ExtractResourcesJsonBody")


@attr.s(auto_attribs=True)
class ExtractResourcesJsonBody:
    """
    Attributes:
        survey (Union[Unset, Survey]): A resource survey of a waypoint, detailing a specific extraction location and the
            types of resources that can be found there.
    """

    survey: Union[Unset, "Survey"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.survey import Survey

        survey: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.survey, Unset):
            survey = self.survey.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if survey is not UNSET:
            field_dict["survey"] = survey

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.survey import Survey

        d = src_dict.copy()
        _survey = d.pop("survey", UNSET)
        survey: Union[Unset, Survey]
        if isinstance(_survey, Unset):
            survey = UNSET
        else:
            survey = Survey.from_dict(_survey)

        extract_resources_json_body = cls(
            survey=survey,
        )

        extract_resources_json_body.additional_properties = d
        return extract_resources_json_body

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
