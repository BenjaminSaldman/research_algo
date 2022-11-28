from typing import Callable
import itertools
import math
import doctest

"""
I was helped by: https://www.geeksforgeeks.org/traveling-salesman-problem-tsp-implementation/amp/
and: https://www.geeksforgeeks.org/travelling-salesman-problem-greedy-approach/
For examples and ideas.

I assumed that all the graphs are hamiltonian.
"""
g = {
    'A': [math.inf, ('B', 10), ('C', 15), ('D', 20)],
    'B': [('A', 10), math.inf, ('C', 35), ('D', 25)],
    'C': [('A', 15), ('B', 35), math.inf, ('D', 30)],
    'D': [('A', 20), ('B', 25), ('C', 30), math.inf]
}
tsp = [[math.inf, 10, 15, 20], [10, math.inf, 35, 25], [15, 35, math.inf, 30], [20, 25, 30, math.inf]]


class Output:
    """
    Output types: we can return the path or the cost of the path.
    """

    def path(items):
        p = ''

        for i in items:
            p += str(i[0]) + ' -> '
        p += str(items[0][0])
        return p[:len(p)]

    def sum(items):
        sum = 0
        for i in items:
            sum += i[1][1]
        return sum


def construct_graph(graph, flag=False):
    """
    Graph constructor for both TSP algorithm.
    The greedy algorithm requires k*n graph and the 'brute force' requires n*n.
    """
    g = []
    ret = []
    if isinstance(graph, dict):
        for j, k in graph.items():
            for i in k:
                if not flag:
                    if i != math.inf:
                        g.append((j, i))
                else:
                    g.append((j, i))
            ret.append(g)
            g = []
    else:
        for i in range(len(graph)):
            for j in range(len(graph[i])):
                if not flag:
                    if graph[i][j] != math.inf:
                        g.append((i, (j, graph[i][j])))
                else:
                    g.append((i, (j, graph[i][j])))
            ret.append(g)
            g = []

    return ret


def TSP_PRINTER(algorithm: Callable, items: list, outputtype=Output.path, flag=False, **kwargs):
    """
    The strategy design pattern, it gets an algorithm, graph, output algorithm and flag
    and returns a path/sum of the hamiltonian cycle.
    >>> TSP_PRINTER(algorithm=greedy_tsp, items=g)
    'A -> B -> D -> C -> A'
    >>> TSP_PRINTER(algorithm=greedy_tsp, items=tsp)
    '0 -> 1 -> 3 -> 2 -> 0'
    >>> TSP_PRINTER(algorithm=greedy_tsp, items=g,outputtype=Output.sum)
    80
    >>> TSP_PRINTER(algorithm=greedy_tsp, items=tsp, outputtype=Output.sum)
    80
    >>> TSP_PRINTER(algorithm=brute_force_tsp, items=g, outputtype=Output.sum, flag=True)
    80
    >>> TSP_PRINTER(algorithm=brute_force_tsp, items=tsp, outputtype=Output.sum, flag=True)
    80
    >>> TSP_PRINTER(algorithm=brute_force_tsp, items=g, outputtype=Output.path, flag=True)
    'A -> B -> D -> C -> A'
    >>> TSP_PRINTER(algorithm=brute_force_tsp, items=tsp, outputtype=Output.path, flag=True)
    '0 -> 1 -> 3 -> 2 -> 0'
    """
    path = algorithm(construct_graph(items, flag), **kwargs)
    return outputtype(path)


def next_row(graph, sym):
    """
    Next row to compute.
    """
    for i in range(len(graph)):
        if graph[i][0][0] == sym:
            return i


def greedy_tsp(graph):
    """
    Greedy algorithm for TSP problem.
    """
    cities = 1  # number of cities we visited.
    min = math.inf  # Minimum cost path.
    visited = {}  # Visited cities.
    for i in range(len(graph)):
        visited[i] = False
    next_city = 0  # Next city to visit.
    row = 0  # Checking next path.
    path = []  # Path we're constructing.
    index = 0  # Current city.
    while cities < len(graph):
        for j in graph[index]:
            """
            If we didn't visit this city (row) and the cost of the edge is minimal
            set it as a candidate.
            """
            if not visited[next_row(graph, j[1][0])] and j[1][1] < min:
                curr = row
                next_city = next_row(graph, j[1][0])
                min = j[1][1]
            row += 1
        cities += 1  # We added one city.
        path.append(graph[index][curr])  # Appending the edge to the path.
        visited[index] = True  # Set the city as visited.
        index = next_city  # Moving to the next city.
        row = 0
        min = math.inf  # The new minimum is infinity.
    path.append(graph[index][0])  # Closing the path to a Hamiltonian cycle.
    return path


def brute_force_tsp(graph):
    """
    'Brute Force' naive solution to the TSP.
    We are starting from the random vertex and find the best
    hamiltonian cycle in the graph moving on all permutations of
    the vertices.
    """
    min_cost = math.inf  # Best cost path.
    curr_path = []  # Current path to compute.
    path = []  # Path to return.
    for j in range(len(graph)):
        nodes = [i for i in range(len(graph))]  # Nodes of the graph without the first.
        nodes.pop(j)
        for perm in itertools.permutations(nodes):
            curr_cost = 0  # Current path cost.
            curr_row = j  # Current vertex we're starting at.
            for i in perm:
                curr_cost += graph[curr_row][i][1][1]  # Adding the cost of the edge.
                curr_path.append(graph[curr_row][i])
                curr_row = i  # Update the next vertex.
            curr_cost += graph[curr_row][j][1][1]  # Closing the cycle.
            curr_path.append(graph[curr_row][j])
            if min_cost > curr_cost:  # Update the minimum cost and the best path to return.
                path = curr_path
                min_cost = curr_cost
            curr_path = []
    return path


if __name__ == '__main__':
    doctest.testmod()
    print(construct_graph(tsp))
    print(construct_graph(g, flag=False))
    print(greedy_tsp(construct_graph(g)))
    print(greedy_tsp(construct_graph(tsp)))
    print(TSP_PRINTER(algorithm=greedy_tsp, items=g))
    print(TSP_PRINTER(algorithm=greedy_tsp, items=g, outputtype=Output.sum))
    print(TSP_PRINTER(algorithm=greedy_tsp, items=tsp))
    print(TSP_PRINTER(algorithm=brute_force_tsp, items=g, outputtype=Output.sum, flag=True))
    print(brute_force_tsp(construct_graph(tsp, flag=True)))
    print(brute_force_tsp(construct_graph(g, flag=True)))
