from enum import Enum


class ContractType(str, Enum):
    PROCUREMENT = "PROCUREMENT"
    SHUTTLE = "SHUTTLE"
    TRANSPORT = "TRANSPORT"

    def __str__(self) -> str:
        return str(self.value)
