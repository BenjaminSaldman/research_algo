from itertools import *
import doctest


class bounded_subsets:
    """
    >>> for s in bounded_subsets([1, 2, 3], 4):  print(s)
    []
    [1]
    [2]
    [3]
    [1, 2]
    [1, 3]
    >>> for s in zip(range(5), bounded_subsets(range(100), 10000000000000000000)): print(s)
    (0, [])
    (1, [0])
    (2, [1])
    (3, [2])
    (4, [3])
    >>> for s in bounded_subsets(range(50, 60), 103): print(s)
    []
    [50]
    [51]
    [52]
    [53]
    [54]
    [55]
    [56]
    [57]
    [58]
    [59]
    [50, 51]
    [50, 52]
    [50, 53]
    [51, 52]

    """

    def __init__(self, S=list, sum=int):
        self.S = sorted(S)
        self.S = [i for i in self.S if i <= sum]  # Sorted array without the numbers that bigger than the sum.
        self.sum = sum
        self.state = []  # Current state is [].
        self.end = None  # None is to end the iterator.
        self.perm = [[]]  # "memory" for the computed permutations.
        self.visited = dict()  # Next size of subset flag.
        self.i = 1  # Current size of subset.
        for i in range(1, len(self.S) + 1):
            self.visited[i] = False

    def __iter__(self):
        return self

    def calc_next(self, i):
        """
        Calculate the next subset with sum <= sum.
        """
        for j in filter(lambda a: (sum(a) <= self.sum), combinations(self.S, i)):
            """
            We iterate over the combinations of size i that their sum is less or equal to the sum the
            iterator got.
            """
            p = [k for k in sorted(j)]
            if p not in self.perm:
                self.perm.append(p)
                self.visited[i] = True
                return p
        if self.visited[i]:
            """
            If we got to here that means we covered all the options of subsets of size i and
            we need to calculate bigger subsets. 
            """
            self.i = i + 1
            return self.calc_next(self.i)
        return None

    def __next__(self):
        if self.state == self.end:
            raise StopIteration

        res = self.state

        self.state = self.calc_next(self.i)

        return res


if __name__ == '__main__':
    doctest.testmod()
    for s in bounded_subsets([1, 2, 3], 4):
        print(s)

    for s in bounded_subsets(range(50, 150), 103):
        print(s)
    for s in bounded_subsets(range(50, 60), 103):
        print(s)
    for s in zip(range(5), bounded_subsets(range(100), 10000000000000000000)):
        print(s)
    for s in bounded_subsets(list(range(90, 100)) + list(range(920, 1000)), 1000):
        print(s)


