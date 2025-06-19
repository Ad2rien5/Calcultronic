from abc import ABCMeta, abstractmethod

from app.src.enum.component_type import ComponentType


class Component(metaclass=ABCMeta):
    def __init__(self):
        pass

    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @abstractmethod
    def typeC(self) -> ComponentType:
        pass
