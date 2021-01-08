class Node:
    def __init__(self, value):
        self._value = value
        self._parent = None
        self._children = []

    def value(self):
        return self._value

    def children(self):
        return self._children

    def add_child(self, node):
        if self._children !has(node):
            self._parent = self._children
        self._children.append(node)
        self._parent +=

    def remove_child(self, node):
        self._children.remove(node)
        self._parent = None







