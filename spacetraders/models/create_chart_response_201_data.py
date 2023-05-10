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
    from ..models.chart import Chart
    from ..models.waypoint import Waypoint


T = TypeVar("T", bound="CreateChartResponse201Data")


@attr.s(auto_attribs=True)
class CreateChartResponse201Data:
    """
    Attributes:
        chart (Chart): The chart of a system or waypoint, which makes the location visible to other agents.
        waypoint (Waypoint): A waypoint is a location that ships can travel to such as a Planet, Moon or Space Station.
    """

    chart: "Chart"
    waypoint: "Waypoint"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.chart import Chart
        from ..models.waypoint import Waypoint

        chart = self.chart.to_dict()

        waypoint = self.waypoint.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "chart": chart,
                "waypoint": waypoint,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.chart import Chart
        from ..models.waypoint import Waypoint

        d = src_dict.copy()
        chart = Chart.from_dict(d.pop("chart"))

        waypoint = Waypoint.from_dict(d.pop("waypoint"))

        create_chart_response_201_data = cls(
            chart=chart,
            waypoint=waypoint,
        )

        create_chart_response_201_data.additional_properties = d
        return create_chart_response_201_data

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
