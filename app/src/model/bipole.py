from app.src.enum.component_type import ComponentType
from app.src.model.component import Component


class Bipole(Component):

    def __init__(self, name: str, typec: ComponentType):
        self.name = name
        self.typec = typec
        self._borneN = None # Node
        self._borneP = None # Node
        self.resistance = None  # Float
        self.intensity = None   # Float
        self.voltage = None  # Float
        self.power = None #Float
        self.state = 0  # -1 open, 0 passing, 1 wire

    def setBorneN(self, borneN):
        self._borneN = borneN
        if self not in self._borneN:
            self._borneN.append(self)

    def setBorneP(self, borneP):
        self._borneP = borneP
        if self not in self._borneP:
            self._borneP.append(self)

    def next(self):
        return self._borneN.next()

    def prev(self):
        return self._borneP.prev()

