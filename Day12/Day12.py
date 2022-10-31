from typing import Dict, Set, List
from queue import SimpleQueue
from VertexMapPoint import VertexMapPoint
from Vertex import Vertex
from DayBase import DayBase, DayBaseSmall


class Day12(DayBase):
    def __init__(self):
        DayBase.__init__(self, 12, to_int=False)

        self.vertices: Dict[str, Vertex] = {}
        for line in self.data:
            a, b = line.split("-")

            if a not in self.vertices:
                self.vertices[a] = Vertex(a)
            if b not in self.vertices:
                self.vertices[b] = Vertex(b)

            self.vertices[a].add_connection(b)
            self.vertices[b].add_connection(a)

    def find_paths(self):
        def _find_paths_inner(current_vertex: VertexMapPoint, current_point: str):
            if current_point.islower() and current_point in current_vertex.current_path:
                return

            current_vertex.add_connection(current_point)

            if current_point == "end":
                return

            for connection in self.vertices[current_point].connections:
                _find_paths_inner(current_vertex.map[current_point], connection)

        start_vertex = VertexMapPoint("start", [])
        for connection in self.vertices["start"].connections:
            _find_paths_inner(start_vertex, connection)

        return start_vertex.count_leaves()

    def find_paths_double_lower(self):
        def _is_valid_point(current_path: List[str], current_point: str):
            if not current_point.islower() or current_point == "start" or current_point == "end":
                return True

            count_dict = {}
            for segment in current_path:
                if not segment.islower() or segment == "start" or segment == "end":
                    continue
                if segment not in count_dict:
                    count_dict[segment] = 0
                count_dict[segment] += 1

            for segment, count in count_dict.items():
                if count == 2:
                    if segment == current_point:  # already used this point twice
                        return False
                    if current_point in count_dict:  # already used a point twice
                        return False
                    break

            return True

        def _find_paths_inner(current_vertex: VertexMapPoint, current_point: str):
            if not _is_valid_point(current_vertex.current_path, current_point):
                return

            current_vertex.add_connection(current_point)

            if current_point == "end":
                return

            for connection in self.vertices[current_point].connections:
                _find_paths_inner(current_vertex.map[current_point], connection)

        start_vertex = VertexMapPoint("start", [])
        for connection in self.vertices["start"].connections:
            _find_paths_inner(start_vertex, connection)

        return start_vertex.count_leaves()

    def part1(self):
        return self.find_paths()

    def part2(self):
        return self.find_paths_double_lower()


day = Day12()
day.run()
