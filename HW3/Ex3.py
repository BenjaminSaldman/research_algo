import doctest


class List:

    def __init__(self, lst=list):
        self._lst = lst

    def __getitem__(self, item):
        """
        >>> List([[[1, 2, 3, 33], [4, 5, 6, 66]],[[7, 8, 9, 99], [10, 11, 12, 122]],[[13, 14, 15, 155], [16, 17, 18, 188]],])[0, 1, 3]
        66
        >>> List([[[1, 2, 3, 33], [4, 5, 6, 66]],[[7, 8, 9, 99], [10, 11, 12, 122]],[[13, 14, 15, 155], [16, 17, 18, 188]],])[0]
        [[1, 2, 3, 33], [4, 5, 6, 66]]
        >>> List([[[1, 2, 3, 33], [4, 5, 6, 66]],[[7, 8, 9, 99], [10, 11, 12, 122]],[[13, 14, 15, 155], [16, 17, 18, 188]],])[1, 1, 3]
        122
        """
        ret = self._lst
        if isinstance(item, tuple):
            for i in item:
                ret = ret[i]
            return ret
        else:
            return ret[item]


mylist = List([
    [[1, 2, 3, 33], [4, 5, 6, 66]],
    [[7, 8, 9, 99], [10, 11, 12, 122]],
    [[13, 14, 15, 155], [16, 17, 18, 188]],
]
)
print(mylist[0, 1, 3])
print(mylist[0])
print(mylist[1, 1, 3])
doctest.testmod()
