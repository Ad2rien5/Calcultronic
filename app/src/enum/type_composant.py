from enum import Enum


class ComponentType(Enum):
    NOEUD = 1
    RESISTANCE = 2
    GENERATEUR_TENSION = 3
    GENERATEUR_COURANT = 4
    INDUCTANCE = 5
    CONDENSATEUR = 6
    INTERUPTEUR = 7
    DIODE = 8
    TRANSISTOR = 9
