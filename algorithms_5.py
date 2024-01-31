import networkx as nx


def is_pareto_efficient(valuations: list[list[float]], allocations: list[list[float]]):
    """
    Part (a) of question 3.
    The function checks if an allocation is Pareto efficient, by iterating over all direct cycles
    and checking if the multiplications of the weights are >=1.
    """
    num_of_players = len(valuations)
    num_of_items = len(valuations[0])
    matrix = []  # Adjacency matrix, each edge is of the form (u,v,weight)
    for i in range(num_of_players):
        for j in range(num_of_players):
            if i == j:
                continue
            indices = [k for k in range(num_of_items) if allocations[i][k] != 0]
            if indices == []: # If player i doesn't have anything in its basket, then there is no edge i->j.
                continue
            # The minimum ratio between some item that is in the basket of i to j.
            val = min(valuations[i][k] / valuations[j][k] for k in indices)
            edge = (i, j, val)
            matrix.append(edge)
    G = nx.DiGraph()  # Creating a directed graph and adding the edges and weights.
    for i in matrix:
        G.add_edge(i[0], i[1], weight=i[2])

    for cycle in nx.simple_cycles(G):  # Iterating over all simple cycles in G.
        weights = []  # Weights of the path.
        a = 1  # The multiplication of the weights
        for i in cycle:
            u, v = cycle[i], cycle[(i + 1) % len(cycle)]  # Getting the edge u->v.
            weight = G.get_edge_data(u, v).get('weight')  # Get the weight of the edge.
            weights.append(weight)
        for i in weights:
            a *= i
        if a < 1:  # If the multiplication of the weights is < 1, it is not Pareto efficient.
            return False
    return True


def is_pareto_efficient_improve(valuations: list[list[float]], allocations: list[list[float]]):
    """
    This function solves part (b) of question 3.
    The code is the same code, but instead of returning False if the allocation
    is not Pareto efficient, it returns a Pareto improvement for the allocations.
    """
    num_of_players = len(valuations)
    num_of_items = len(valuations[0])
    matrix = []
    items = dict()
    for i in range(num_of_players):
        for j in range(num_of_players):
            if i == j:
                continue
            indices = [k for k in range(num_of_items) if allocations[i][k] != 0]
            if indices == []:
                continue
            val = min(valuations[i][k] / valuations[j][k] for k in indices)
            edge = (i, j, val)
            item = min(indices, key=lambda k: valuations[i][k] / valuations[j][k])  # The index of the item.
            edge2 = (i, j, item)
            matrix.append(edge)
            items[(i, j)] = edge2
    G = nx.DiGraph()
    for i in matrix:
        G.add_edge(i[0], i[1], weight=i[2])

    for cycle in nx.simple_cycles(G):
        weights = []
        a = 1
        for i in cycle:
            u, v = cycle[i], cycle[(i + 1) % len(cycle)]
            weight = G.get_edge_data(u, v).get('weight')
            weights.append(weight)
        for i in weights:
            a *= i
        if a < 1:
            epsilon = 1 / 1000  # Player A chooses e from x.
            for i in cycle:
                u, v = cycle[i], cycle[(i + 1) % len(cycle)]
                weight = G.get_edge_data(u, v).get('weight')
                item = items[(u, v)][2]
                allocations[v][item] += epsilon * valuations[u][item]  # A gives B e part from x.
                allocations[u][item] -= epsilon * valuations[u][item]
                epsilon = epsilon / weight  # For B it equals to e/r and so on.
            return allocations
    return True


print(is_pareto_efficient_improve(
    valuations=[[10, 20, 30, 40], [40, 30, 20, 10]], allocations=[[1, 0.7, 1, 0], [0, 0.3, 0, 0]]))
print(is_pareto_efficient_improve(
    valuations=[[10, 20, 30, 40], [40, 30, 20, 10]], allocations=[[1, 1, 1, 1], [0, 0, 0, 0]]))
