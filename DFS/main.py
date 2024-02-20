from typing import List, Dict


def dfs_recursive(graph: Dict[int, List[int]], vertex: int, visited=None) -> List[int]:
    if visited is None:
        visited = []

    visited.append(vertex)

    for neighbour in graph[vertex]:
        if neighbour not in visited:
            dfs_recursive(graph, neighbour, visited)
    return visited


def dfs_iterative(graph: Dict[int, List[int]], vertex: int) -> List[int]:
    stack = [vertex]
    visited = []

    while stack:
        vertex = stack.pop()

        if vertex not in visited:
            visited.append(vertex)
            for neighbour in graph[vertex][::-1]:
                stack.append(neighbour)

    return visited


def is_acyclic(graph: Dict[int, List[int]]) -> bool:
    visited = []
    for vertex, neighbours in graph.items():
        for neighbour in neighbours:
            if neighbour in visited:
                return False
            if vertex not in visited:
                visited.append(vertex)
    return True


if __name__ == '__main__':
    G = {
        1: [2, 3, 5],
        2: [1, 4, 6],
        3: [1, 7],
        4: [2],
        5: [1, 6],
        6: [2, 5],
        7: [3]
    }

    Graphs = [{1: [2, 3], 3: [4]}, {1: [2], 2: [3], 3: [1]},
              {2: [1, 3], 3: [2]}, {1: [2], 3: [2, 4], 4: [3]},
              {1: [2, 3], 2: [4], 3: [4]}, {1: [2, 3], 2: [3]},
              {1: [2], 2: [3], 3: [1, 4]}]

    # res = dfs_recursive(G, 1)
    # print(res)
    # res = dfs_iterative(G, 1)
    # print(res)

    for graph in Graphs:
        print(graph, is_acyclic(graph))
