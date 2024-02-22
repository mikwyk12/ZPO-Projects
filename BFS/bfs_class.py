from typing import List, Set, Dict
from enum import Enum, auto
from collections import deque

VertexID = int
AdjList = Dict[VertexID, List[VertexID]]
Distance = int


class Color(Enum):
    WHITE = auto()
    GRAY = auto()
    BLACK = auto()


def neighbors(adjlist: AdjList, start_vertex_id: VertexID,
              max_distance: Distance) -> Set[VertexID]:
    color = {}
    q = deque([(start_vertex_id, 0)])
    result = set()

    for u in adjlist.keys():
        color[u] = Color.WHITE

    color[start_vertex_id] = Color.GRAY

    while q:
        u, d = q.popleft()

        if 0 < d <= max_distance:
            result.add(u)

        if u in adjlist.keys():
            for v in adjlist[u]:
                if v not in color:
                    color[v] = Color.WHITE

                if color[v] == Color.WHITE:
                    color[v] = Color.GRAY
                    q.append((v, d + 1))

            color[u] = Color.BLACK

    return result
