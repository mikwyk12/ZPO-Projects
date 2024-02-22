from tabulate import tabulate
from bfs_class import *


def procedure():
    G = {
        1: [2, 4],
        2: [3],
        4: [5],
        5: [2, 6],
        7: [1]
    }
    vertex_id = 1
    distance = [1, 2]
    result = []

    for d in distance:
        result.append(neighbors(G, vertex_id, d))

    print(f"Graph: {G}\n")
    print(tabulate({"Distance": distance, "Neighbours": result}, headers="keys", tablefmt="github"))


if __name__ == '__main__':
    procedure()
