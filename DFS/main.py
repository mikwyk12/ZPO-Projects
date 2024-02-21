from tabulate import tabulate
from dfs import *


def procedure() -> None:
    print("Adjacency matrix:")
    print(tabulate(A, tablefmt="plain"))
    print(f"Adjacency list:\n{adjmat_to_adjlist(A)}\n")
    print("Adjacency matrix:")
    print(tabulate(B, tablefmt="plain"))
    print(f"Adjacency list:\n{adjmat_to_adjlist(B)}\n")

    print(f"Graph: {G}")
    print(f"DFS recursive: {dfs_recursive(G, 1)}")
    print(f"DFS iterative: {dfs_iterative(G, 1)}\n")

    result = []
    for graph in Graphs:
        result.append(is_acyclic(graph))

    print(tabulate({"Graphs": Graphs, "is_acyclic?": result}, headers="keys", tablefmt="github"))


if __name__ == '__main__':
    A = [
        [0, 1, 0],
        [0, 0, 1],
        [1, 2, 0]
    ]

    B = [
        [0, 1],
        [0, 0]
    ]

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

    procedure()
