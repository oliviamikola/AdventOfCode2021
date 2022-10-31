from typing import Set


class Vertex:
    def __init__(self, point: str):
        self.name: str = point
        self.connections: Set[str] = set()

    def __str__(self):
        return "%s: %s" % (self.name, self.connections)

    def add_connection(self, other_point: str):
        if other_point == "start":
            return

        self.connections.add(other_point)
