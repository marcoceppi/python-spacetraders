from typing import (
    Any,
    Dict,
    List,
    TypeVar,
    Union,
)

from pydantic import BaseModel, Field

from ..models.system_type import SystemType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ConnectedSystem")


class ConnectedSystem(BaseModel):
    """
    Attributes:
        symbol (str): The symbol of the system.
        sector_symbol (str): The sector of this system.
        type (SystemType): The type of waypoint.
        x (int): Position in the universe in the x axis.
        y (int): Position in the universe in the y axis.
        distance (int): The distance of this system to the connected Jump Gate.
        faction_symbol (Union[Unset, str]): The symbol of the faction that owns the connected jump gate in the system.
    """

    symbol: str = Field(alias="symbol")
    sector_symbol: str = Field(alias="sectorSymbol")
    type: SystemType = Field(alias="type")
    x: int = Field(alias="x")
    y: int = Field(alias="y")
    distance: int = Field(alias="distance")
    faction_symbol: Union[Unset, str] = Field(UNSET, alias="factionSymbol")
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
