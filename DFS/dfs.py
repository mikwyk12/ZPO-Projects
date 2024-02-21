from typing import List, Dict


def adjmat_to_adjlist(adjmat: List[List[int]]) -> Dict[int, List[int]]:
    adjlist = dict(enumerate(adjmat, start=1))
    num = len(adjlist)

    for key, value in adjlist.items():
        temp = []
        for j in range(num):
            if value[j] != 0:
                for k in range(value[j]):
                    temp.append(j + 1)
        adjlist[key] = temp

    for key in range(1, num + 1):
        if not adjlist[key]:
            del adjlist[key]
    return adjlist


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
