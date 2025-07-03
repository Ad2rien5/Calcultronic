from app.src.enum.component_type import ComponentType
from app.src.model.component import Component


class Node(Component):

    def __init__(self, name: str, **components: Component):
        self.names = name
        self.typeC = ComponentType.NODE
        self.components = []

        for compo in components:
            self.components.append(compo)

    def __contains__(self, item):

        match item:
            case str():
                return item in [i.name for i in self.components]

            case Component():
                return item in [i for i in self.components]

        raise ValueError(f"Cannot compare Component object with {type(item)}.")

    def add(self, component: Component):
        self.components.append(component)

    def remove(self, component: Component):
        for i in range(len(self.components)):
            if self.components[i] == component:
                return self.components.pop(i)
        return None