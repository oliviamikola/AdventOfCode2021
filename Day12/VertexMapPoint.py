from typing import List, Set, Dict


class VertexMapPoint:
    def __init__(self, level: str, current_path: List[str], path_connections: Set[str] = None):
        self.level: str = level
        self.current_path = current_path + [level]

        if path_connections:
            self.map: Dict[str, VertexMapPoint] = {p: VertexMapPoint(p, self.current_path) for p in path_connections}
        else:
            self.map = {}

    def count_leaves(self):
        total = 0
        for point, point_map in self.map.items():
            if point_map.level == "end":
                total += 1
            else:
                total += point_map.count_leaves()

        return total

    def add_connection(self, point: str):
        if point not in self.map:
            self.map[point] = VertexMapPoint(point, self.current_path)
