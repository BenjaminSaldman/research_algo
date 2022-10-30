import doctest
from queue import Queue


# Ex1
def safe_call(f, **kwargs):
    """
    >>> safe_call(f,x=5,y=7.0,z=3)
    15.0
    >>> safe_call(f=f,x=5,y=False,z=3)
    Traceback (most recent call last):
        ...
    Exception
    >>> safe_call(g, x=2, y=3, z=2, k=3)
    16
    >>> safe_call(g, x=2, y=3, z=2, k=1.0)
    Traceback (most recent call last):
        ...
    Exception

    :param f:
    :param kwargs:
    :return:
    """
    for i, j in kwargs.items():  # Kwargs is a dict
        if i in f.__annotations__.keys():  # Checking if the value is in the annotations of the function
            if f.__annotations__[i] != type(
                    j):  # If the type of the annotation is not the same as the input, raise an exception.
                raise Exception
    return f(**kwargs)  # Unpack the kwargs and call f with the values.


def f(x: int, y: float, z):
    return x + y + z


def g(x: int, y: int, z: int, k: int):
    return x ** y + z ** k


print(f"Ex1 Examples: ")
print(safe_call(f=f, x=5, y=7.0, z=3))
try:
    print(safe_call(f=f, x=5, y=False, z=3))
except:
    print(f"y didn't get float")
print(safe_call(g, x=2, y=3, z=2, k=3))

print(f"############################################################")


# Ex2
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


def sort_dict(d):
    """

    :param d: a dictionary.
    :return: a sorted dictionary by keys.
    """
    try:
        k = dict(d)
        k = sorted(k)
        ans = {}
        for i in k:
            ans[i] = d[i]
        return ans
    except:
        raise Exception


def calc_sorted(d):
    """
    recursive function that sorts a data-structure d
    in all levels
    :param d:
    :return: sorted data structures in all levels.
    """

    """
    Stop conditions, where the d non-iterable.
    """
    try:
        if type(d) == str:
            raise Exception
        iter(d)
    except:
        return d
    """
        converting tuples and sets to list because we can't
        modify this data structures.
    """
    y = 0
    if type(d) == tuple:
        y = 1
        d = list(d)
    elif type(d) == set:
        y = 2
        d = list(d)

    try:
        """
            Trying to sort the data structure,
            if we can't we recursively trying to 
            sort every element in the data structure.
        """
        if type(d) == dict:
            d = sort_dict(d)
            for i, j in d.items():
                try:
                    if type(d[i]) != str:
                        d[i] = sorted(d[i])

                except:
                    d[i] = calc_sorted(d[i])
        else:

            d = sorted(d)
            for i in range(len(d)):
                try:

                    if type(d[i]) != str:
                        d[i] = sorted(d[i])

                except:
                    d[i] = calc_sorted(d[i])



    except:
        if type(d) == dict:
            for i, j in d.items():
                d[i] = calc_sorted(j)
        else:
            for i in range(len(d)):
                d[i] = calc_sorted(d[i])
    """
        Converting the data structures back to their original type.
    """
    if y == 1:
        d = tuple(d)
    elif y == 2:
        d = set(d)
    return d


def print_sorted(d):
    """
     >>> print_sorted(x)
     {'a': 5, 'b': [1, 2, 3, 4], 'c': [6, (3, 4, 5), 5]}
     >>> print_sorted(y)
     ([6, {3, 4, 5}, 5], 5, (1, 2, 3, 4))
     >>> print_sorted(z)
     [([6, {3, 4, 5}, 5], 5, (1, 2, 3, 4)), {'a': 5, 'b': [1, 2, 3, 4], 'c': [6, (3, 4, 5), 5]}]

    :param d:
    :return:
    """
    print(calc_sorted(d))


x = {"a": 5, "c": [6, (4, 3, 5), 5], "b": (1, 3, 2, 4)}
y = ([6, {4, 3, 5}, 5], 5, (1, 3, 2, 4))
z = [y, x]
print(f"Ex3 Examples: ")
print_sorted(x)
print_sorted(y)
print_sorted(z)
print(f"############################################################")
print(f"Ex4 solution + picture is in the github and here is the link: https://www.codingame.com/training/easy/blowing-fuse/solution?id=26986264 ")

doctest.testmod(verbose=True)
