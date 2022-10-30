import doctest
from queue import Queue


def breadth_first_search(start, end, neighbor_function):
    """
     >>> breadth_first_search(start=(0, 0), end=(2, 2), neighbor_function=four_neighbor_function)
     [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)]
     >>> breadth_first_search(start=(0, 0), end=(2, 2), neighbor_function=x_powers)
     [(0, 0), (1, 1), (2, 2)]
     >>> breadth_first_search(start=(0, 0, 0), end=(2, 2, 2), neighbor_function=three_neighbors)
     [(0, 0, 0), (1, 0, 0), (2, 0, 0), (3, 0, 0), (4, 0, 0), (5, 0, 0), (6, 0, 0), (5, 0, 1), (4, 0, 2), (3, 0, 3), (2, 0, 4), (2, 1, 3), (2, 2, 2)]

     I used the pseudocode of BFS and dijkstra algorithm from wikipedia:
     https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm
     https://en.wikipedia.org/wiki/Breadth-first_search
     Dijkstra is to construct the path and BFS to simulate dijkstra
     on unweighted graph.
     """
    q = Queue()  # Queue to BFS algorithm
    prev = {}  # parent dict: key=node value=parent.
    visited = [start]  # all visited nodes.
    q.put(start)  # starting the scan with the first node.
    while not q.empty():
        x = q.get()
        if x == end:
            break
        for y in neighbor_function(x):
            if y not in visited:
                visited.append(y)
                q.put(y)
                prev[y] = x
    S = []  # empty 'stack' or sequence.
    u = end  # current node.
    while u in prev:
        S.append(u)
        u = prev[u]
    S.append(start)
    seq = []  # path to return
    for i in range(len(S)):
        seq.append(S.pop())
    return seq


def four_neighbor_function(node):
    (x, y) = node
    return [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]


def x_powers(node):
    (x, y) = node
    return [(x ** 2 + 1, y ** 2 + 1)]


def three_neighbors(node):
    (x, y, z) = node
    return [(x + 1, y, z), (x - 1, y, z + 1), (x, y + 1, z - 1)]


print(f"Ex2 examples: ")
print(breadth_first_search(start=(0, 0), end=(2, 2), neighbor_function=four_neighbor_function))
print(breadth_first_search(start=(0, 0), end=(2, 2), neighbor_function=x_powers))
print(breadth_first_search(start=(0, 0, 0), end=(2, 2, 2), neighbor_function=three_neighbors))
print(f"############################################################")

doctest.testmod(verbose=True)
