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
    from ..models.connected_system import ConnectedSystem


T = TypeVar("T", bound="JumpGate")


@attr.s(auto_attribs=True)
class JumpGate:
    """
    Attributes:
        jump_range (float): The maximum jump range of the gate.
        connected_systems (List['ConnectedSystem']): The systems within range of the gate that have a corresponding
            gate.
        faction_symbol (Union[Unset, str]): The symbol of the faction that owns the gate.
    """

    jump_range: float
    connected_systems: List["ConnectedSystem"]
    faction_symbol: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.connected_system import ConnectedSystem

        jump_range = self.jump_range
        connected_systems = []
        for connected_systems_item_data in self.connected_systems:
            connected_systems_item = connected_systems_item_data.to_dict()

            connected_systems.append(connected_systems_item)

        faction_symbol = self.faction_symbol

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "jumpRange": jump_range,
                "connectedSystems": connected_systems,
            }
        )
        if faction_symbol is not UNSET:
            field_dict["factionSymbol"] = faction_symbol

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.connected_system import ConnectedSystem

        d = src_dict.copy()
        jump_range = d.pop("jumpRange")

        connected_systems = []
        _connected_systems = d.pop("connectedSystems")
        for connected_systems_item_data in _connected_systems:
            connected_systems_item = ConnectedSystem.from_dict(
                connected_systems_item_data
            )

            connected_systems.append(connected_systems_item)

        faction_symbol = d.pop("factionSymbol", UNSET)

        jump_gate = cls(
            jump_range=jump_range,
            connected_systems=connected_systems,
            faction_symbol=faction_symbol,
        )

        jump_gate.additional_properties = d
        return jump_gate

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
