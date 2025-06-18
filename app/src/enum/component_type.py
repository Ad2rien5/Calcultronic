from enum import Enum


class ComponentType(Enum):
    NODE = 1
    RESISTOR = 2
    VOLTAGE_GENERATOR = 3
    CURRENT_GENERATOR = 4
    INDUCTOR = 5
    CAPACITOR = 6
    SWITCH = 7
    DIODE = 8
    TRANSISTOR = 9
