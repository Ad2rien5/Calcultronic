from abc import ABCMeta, abstractmethod, abstractproperty

from app.src.enum.component_type import ComponentType


class Component(metaclass=ABCMeta):
    name: str
    typec: ComponentType
