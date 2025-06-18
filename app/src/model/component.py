from abc import ABCMeta, abstractmethod

from app.src.enum.type_composant import ComponentType


class Component(metaclass=ABCMeta):
    def __init__(self):
        pass

    @property
    @abstractmethod
    def nom(self) -> str:
        pass

    @abstractmethod
    def typeC(self) -> ComponentType:
        pass
