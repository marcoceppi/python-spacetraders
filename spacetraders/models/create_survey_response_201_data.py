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
    from ..models.cooldown import Cooldown
    from ..models.survey import Survey


T = TypeVar("T", bound="CreateSurveyResponse201Data")


@attr.s(auto_attribs=True)
class CreateSurveyResponse201Data:
    """
    Attributes:
        cooldown (Cooldown): A cooldown is a period of time in which a ship cannot perform certain actions.
        surveys (List['Survey']):
    """

    cooldown: "Cooldown"
    surveys: List["Survey"]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.cooldown import Cooldown
        from ..models.survey import Survey

        cooldown = self.cooldown.to_dict()

        surveys = []
        for surveys_item_data in self.surveys:
            surveys_item = surveys_item_data.to_dict()

            surveys.append(surveys_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "cooldown": cooldown,
                "surveys": surveys,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.cooldown import Cooldown
        from ..models.survey import Survey

        d = src_dict.copy()
        cooldown = Cooldown.from_dict(d.pop("cooldown"))

        surveys = []
        _surveys = d.pop("surveys")
        for surveys_item_data in _surveys:
            surveys_item = Survey.from_dict(surveys_item_data)

            surveys.append(surveys_item)

        create_survey_response_201_data = cls(
            cooldown=cooldown,
            surveys=surveys,
        )

        create_survey_response_201_data.additional_properties = d
        return create_survey_response_201_data

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
