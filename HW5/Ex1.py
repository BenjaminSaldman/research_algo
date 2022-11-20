from itertools import *


class bounded_subsets:
    def __init__(self, S=list, sum=int):
        self.S = sorted(S)
        self.sum = sum
        self.state = []
        self.end = None
        for i in self.S:
            if i > self.sum:
                self.S.remove(i)
        self.curr_sum = 0
        self.perm = [[]]
        self.curr = []
        self.visited = dict()
        self.i = 1
        for i in range(1, len(self.S) + 1):
            self.visited[i] = False

    def __iter__(self):
        return self

    def get_sum(t):
        sum = 0
        for i in t:
            sum += t
        return sum

    def calc_next(self, i):

        for j in sorted(filter(lambda a: (sum(a) <= self.sum) and [f for f in sorted(a)] not in self.perm,
                               combinations(self.S, i)), key=sum):
            p = [k for k in sorted(j)]
            if p not in self.perm:
                self.perm.append(p)
                self.visited[i] = True
                return p
        if self.visited[i]:
            self.i = i
            return self.calc_next(i + 1)
        return None

    def __next__(self):
        if self.state == self.end:
            raise StopIteration

        res = self.state

        self.state = self.calc_next(self.i)

        return res


if __name__ == '__main__':
    t = bounded_subsets([1, 2, 3], 4)
    for s in t:
        print(s)

    for s in bounded_subsets(range(50, 150), 103):
        print(s)
    for s in zip(range(5), bounded_subsets(range(100), 10000000000000000000)):
        print(s)
