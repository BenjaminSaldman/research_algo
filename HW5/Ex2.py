from typing import Callable, Any

import math


class Output:
    def path(items):
        p = ''
        for i in items:
            p += i[0] + ' -> '
        return p[:len(p) - 3]

    def sum(items):
        sum = 0
        for i in items:
            sum += i[1][1]
        return sum


def construct_graph(graph):
    g = []
    ret = []
    if isinstance(graph, dict):
        for j, k in graph.items():
            for i in k:
                g.append((j, i))
            ret.append(g)
            g = []
    else:
        for i in range(len(graph)):
            for j in range(len(graph[i])):
                if graph[i][j] != math.inf:
                    g.append((i, (j, graph[i][j])))
            ret.append(g)
            g = []

    return ret


def TSP_PRINTER(algorithm: Callable, items: list, outputtype=Output.path, **kwargs):
    path = algorithm(construct_graph(items), **kwargs)
    return outputtype(path)


def next_row(graph, sym):
    for i in range(len(graph)):
        if graph[i][0][0] == sym:
            return i


def greedy_tsp(graph):
    cities = 1
    min = math.inf
    visited = {}
    for i in range(len(graph) + 1):
        visited[i] = False
    col = 0
    row = 0
    path = []
    index = 0
    while cities < len(graph):
        for j in graph[index]:
            if not visited[next_row(graph, j[1][0])] and j[1][1] < min:
                next = row
                col = next_row(graph, j[1][0])
                min = j[1][1]
            row += 1
        cities += 1
        path.append(graph[index][next])
        visited[index] = True
        index = col
        row = 0
        min = math.inf
    path.append(graph[index][0])
    return path


if __name__ == '__main__':
    g = {
        'A': [('B', 10), ('C', 15), ('D', 20)],
        'B': [('A', 10), ('C', 35), ('D', 25)],
        'C': [('A', 15), ('B', 35), ('D', 30)],
        'D': [('A', 20), ('B', 25), ('C', 30)]
    }
    tsp = [[math.inf, 10, 15, 20], [10, math.inf, 35, 25], [15, 35, math.inf, 30], [20, 25, 30, math.inf]]
    print(construct_graph(tsp))
    print(construct_graph(g))
    print(greedy_tsp(construct_graph(g)))
    print(greedy_tsp(construct_graph(tsp)))
    print(TSP_PRINTER(algorithm=greedy_tsp, items=g))
    print(TSP_PRINTER(algorithm=greedy_tsp, items=g, outputtype=Output.sum))
    # print(construct_graph(tsp))
