from enum import Enum


class FactionSymbol(str, Enum):
    AEGIS = "AEGIS"
    ANCIENTS = "ANCIENTS"
    ASTRO = "ASTRO"
    COBALT = "COBALT"
    CORSAIRS = "CORSAIRS"
    COSMIC = "COSMIC"
    CULT = "CULT"
    DOMINION = "DOMINION"
    ECHO = "ECHO"
    ETHEREAL = "ETHEREAL"
    GALACTIC = "GALACTIC"
    LORDS = "LORDS"
    OBSIDIAN = "OBSIDIAN"
    OMEGA = "OMEGA"
    QUANTUM = "QUANTUM"
    SHADOW = "SHADOW"
    SOLITARY = "SOLITARY"
    UNITED = "UNITED"
    VOID = "VOID"

    def __str__(self) -> str:
        return str(self.value)
