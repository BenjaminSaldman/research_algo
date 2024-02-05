import networkx as nx
import doctest
import math


def is_pareto_efficient(valuations: list[list[float]], allocations: list[list[float]]):
    """
    Part (a) of question 3.
    The function checks if an allocation is Pareto efficient, by iterating over all direct cycles
    and checking if the multiplications of the weights are >=1.

    >>> is_pareto_efficient(valuations=[[10, 20, 30, 40], [40, 30, 20, 10]], allocations=[[1, 1, 1, 1], [0, 0, 0, 0]])
    True
    >>> is_pareto_efficient_improve(valuations=[[10, 20, 30, 40], [40, 30, 20, 10]], allocations=[[1, 1, 1, 1], [0, 0, 0, 0]])
    True
    >>> is_pareto_efficient_improve(valuations=[[10, 20, 30, 40], [40, 30, 20, 10]], allocations=[[0, 0, 0, 0], [1, 1, 1, 1]])
    True
    >>> is_pareto_efficient(valuations=[[10, 20, 30, 40], [40, 30, 20, 10]], allocations=[[1, 0.7, 1, 0], [0, 0.3, 0, 0]])
    False
    >>> is_pareto_efficient(valuations=[[10, 20, 30, 40], [40, 30, 20, 10], [40, 30, 20, 10]],allocations=[[1, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]])
    False
    >>> is_pareto_efficient_improve(valuations=[[10, 20, 30, 40], [40, 30, 20, 10],[40, 30, 20, 10]], allocations=[[0, 0, 0, 0],[0, 0, 0, 0], [1, 1, 1, 1]])
    True
    """
    num_of_players = len(valuations)
    num_of_items = len(valuations[0])
    matrix = []  # Adjacency matrix, each edge is of the form (u,v,weight).
    for i in range(num_of_players):
        for j in range(num_of_players):
            if i == j:
                continue
            indices = [k for k in range(num_of_items) if allocations[i][k] != 0]
            if indices == []:  # If player i doesn't have anything in its basket, then there is no edge i->j.
                continue
            # The minimum ratio between some item that is in the basket of i to j.
            val = min(math.log(valuations[i][k] / valuations[j][k], math.e) for k in indices)
            edge = (i, j, val)
            matrix.append(edge)
    G = nx.DiGraph()  # Creating a directed graph and adding the edges and weights.
    for i in matrix:
        G.add_edge(i[0], i[1], weight=i[2])
    return not nx.negative_edge_cycle(G)  # The function returns true if there exists a negative cycle.


def is_pareto_efficient_improve(valuations: list[list[float]], allocations: list[list[float]]):
    """
    This function solves part (b) of question 3.
    The code is the same code, but instead of returning False if the allocation
    is not Pareto efficient, it returns a Pareto improvement for the allocations.

    >>> is_pareto_efficient_improve(valuations=[[10, 20, 30, 40], [40, 30, 20, 10],[40, 30, 20, 10]], allocations=[[0, 0, 0, 0],[0, 0, 0, 0], [1, 1, 1, 1]])
    True
    >>> is_pareto_efficient_improve(valuations=[[10, 20, 30, 40], [40, 30, 20, 10]], allocations=[[1, 0.7, 1, 0], [0, 0.3, 0, 0]])
    [[0.99, 0.82, 1, 0], [0.01, 0.18, 0, 0]]
    >>> is_pareto_efficient_improve(valuations=[[10, 20, 30, 40], [40, 30, 20, 10], [40, 30, 20, 10]],allocations=[[1, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]])
    [[0.99, 1, 0, 0.04], [0.01, 0, 0, 0.96], [0, 0, 1, 0]]
    """
    num_of_players = len(valuations)
    num_of_items = len(valuations[0])
    matrix = []
    matrix2 = []
    items = dict()
    for i in range(num_of_players):
        for j in range(num_of_players):
            if i == j:
                continue
            indices = [k for k in range(num_of_items) if allocations[i][k] != 0]
            if indices == []:
                continue
            val = min(math.log(valuations[i][k] / valuations[j][k], math.e) for k in indices)
            edge = (i, j, val)
            item = min(indices,
                       key=lambda k: math.log(valuations[i][k] / valuations[j][k], math.e))  # The index of the item.
            edge2 = (i, j, item)
            matrix.append(edge)
            items[(i, j)] = edge2
            val_normal = min(valuations[i][k] / valuations[j][k] for k in indices)
            edge_normal = (i, j, val_normal)
            matrix2.append(edge_normal)
    G = nx.DiGraph()
    G_weights = nx.DiGraph()
    for i in matrix:
        G.add_edge(i[0], i[1], weight=i[2])
    for i in matrix2:
        G_weights.add_edge(i[0], i[1], weight=i[2])
    cycles = []
    for i in matrix:
        try:
            c = nx.find_negative_cycle(G, i[0])
            cycles.append(c)
        except:
            continue
    if cycles == []:
        return True
    cycle = cycles[0]
    epsilon = 1 / 1000  # Player A chooses e from x.
    for i in range(len(cycle) - 1):
        u, v = cycle[i], cycle[(i + 1)]  # Getting the edge u->v.
        weight = G_weights.get_edge_data(u, v).get('weight')
        item = items[(u, v)][2]  # Item X of A which we added the edge A->B.
        allocations[v][item] += epsilon * valuations[u][item]  # A gives B e part from x.
        allocations[u][item] -= epsilon * valuations[u][item]  # Decrease from A the part it gave to B.
        epsilon = epsilon / weight  # For B it equals to e/r and so on.
    return allocations  # Return the pareto improvement allocation.


if __name__ == '__main__':
    doctest.testmod(verbose=True)
