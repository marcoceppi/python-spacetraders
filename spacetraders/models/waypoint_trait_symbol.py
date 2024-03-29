from enum import Enum


class WaypointTraitSymbol(str, Enum):
    ASH_CLOUDS = "ASH_CLOUDS"
    BARREN = "BARREN"
    BLACK_MARKET = "BLACK_MARKET"
    BREATHABLE_ATMOSPHERE = "BREATHABLE_ATMOSPHERE"
    BUREAUCRATIC = "BUREAUCRATIC"
    CANYONS = "CANYONS"
    COMMON_METAL_DEPOSITS = "COMMON_METAL_DEPOSITS"
    CORROSIVE_ATMOSPHERE = "CORROSIVE_ATMOSPHERE"
    CORRUPT = "CORRUPT"
    CRUSHING_GRAVITY = "CRUSHING_GRAVITY"
    DEBRIS_CLUSTER = "DEBRIS_CLUSTER"
    DEEP_CRATERS = "DEEP_CRATERS"
    DIVERSE_LIFE = "DIVERSE_LIFE"
    DRY_SEABEDS = "DRY_SEABEDS"
    EXPLORATION_OUTPOST = "EXPLORATION_OUTPOST"
    EXPLOSIVE_GASES = "EXPLOSIVE_GASES"
    EXTREME_PRESSURE = "EXTREME_PRESSURE"
    EXTREME_TEMPERATURES = "EXTREME_TEMPERATURES"
    FOSSILS = "FOSSILS"
    FROZEN = "FROZEN"
    HIGH_TECH = "HIGH_TECH"
    HOLLOWED_INTERIOR = "HOLLOWED_INTERIOR"
    ICE_CRYSTALS = "ICE_CRYSTALS"
    INDUSTRIAL = "INDUSTRIAL"
    JOVIAN = "JOVIAN"
    JUNGLE = "JUNGLE"
    MAGMA_SEAS = "MAGMA_SEAS"
    MARKETPLACE = "MARKETPLACE"
    MEGA_STRUCTURES = "MEGA_STRUCTURES"
    METHANE_POOLS = "METHANE_POOLS"
    MICRO_GRAVITY_ANOMALIES = "MICRO_GRAVITY_ANOMALIES"
    MILITARY_BASE = "MILITARY_BASE"
    MINERAL_DEPOSITS = "MINERAL_DEPOSITS"
    MUTATED_FLORA = "MUTATED_FLORA"
    OCEAN = "OCEAN"
    OUTPOST = "OUTPOST"
    OVERCROWDED = "OVERCROWDED"
    PERPETUAL_DAYLIGHT = "PERPETUAL_DAYLIGHT"
    PERPETUAL_OVERCAST = "PERPETUAL_OVERCAST"
    PIRATE_BASE = "PIRATE_BASE"
    PRECIOUS_METAL_DEPOSITS = "PRECIOUS_METAL_DEPOSITS"
    RADIOACTIVE = "RADIOACTIVE"
    RARE_METAL_DEPOSITS = "RARE_METAL_DEPOSITS"
    RESEARCH_FACILITY = "RESEARCH_FACILITY"
    ROCKY = "ROCKY"
    SALT_FLATS = "SALT_FLATS"
    SCARCE_LIFE = "SCARCE_LIFE"
    SCATTERED_SETTLEMENTS = "SCATTERED_SETTLEMENTS"
    SHALLOW_CRATERS = "SHALLOW_CRATERS"
    SHIPYARD = "SHIPYARD"
    SPRAWLING_CITIES = "SPRAWLING_CITIES"
    STRIPPED = "STRIPPED"
    STRONG_GRAVITY = "STRONG_GRAVITY"
    STRONG_MAGNETOSPHERE = "STRONG_MAGNETOSPHERE"
    SUPERVOLCANOES = "SUPERVOLCANOES"
    SURVEILLANCE_OUTPOST = "SURVEILLANCE_OUTPOST"
    SWAMP = "SWAMP"
    TEMPERATE = "TEMPERATE"
    TERRAFORMED = "TERRAFORMED"
    THIN_ATMOSPHERE = "THIN_ATMOSPHERE"
    TOXIC_ATMOSPHERE = "TOXIC_ATMOSPHERE"
    TRADING_HUB = "TRADING_HUB"
    UNCHARTED = "UNCHARTED"
    UNDER_CONSTRUCTION = "UNDER_CONSTRUCTION"
    UNSTABLE_COMPOSITION = "UNSTABLE_COMPOSITION"
    VAST_RUINS = "VAST_RUINS"
    VIBRANT_AURORAS = "VIBRANT_AURORAS"
    VOLCANIC = "VOLCANIC"
    WEAK_GRAVITY = "WEAK_GRAVITY"

    def __str__(self) -> str:
        return str(self.value)
