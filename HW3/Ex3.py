import doctest


class List(list):

    def __init__(self, *args):
        super().__init__(*args)
        # self._lst = lst

    def __getitem__(self, item):
        """
        >>> List([[[1, 2, 3, 33], [4, 5, 6, 66]],[[7, 8, 9, 99], [10, 11, 12, 122]],[[13, 14, 15, 155], [16, 17, 18, 188]],])[0, 1, 3]
        66
        >>> List([[[1, 2, 3, 33], [4, 5, 6, 66]],[[7, 8, 9, 99], [10, 11, 12, 122]],[[13, 14, 15, 155], [16, 17, 18, 188]],])[0]
        [[1, 2, 3, 33], [4, 5, 6, 66]]
        >>> List([[[1, 2, 3, 33], [4, 5, 6, 66]],[[7, 8, 9, 99], [10, 11, 12, 122]],[[13, 14, 15, 155], [16, 17, 18, 188]],])[1, 1, 3]
        122
        """
        if isinstance(item, tuple):
            ret = super().__getitem__(item[0])
            for i in item[1:]:
                ret = ret[i]
            return ret
        else:
            return super().__getitem__(item)

    def __setitem__(self, key, value):
        pass


mylist = List([
    [[1, 2, 3, 33], [4, 5, 6, 66]],
    [[7, 8, 9, 99], [10, 11, 12, 122]],
    [[13, 14, 15, 155], [16, 17, 18, 188]],
]
)
print(mylist)
print(len(mylist))
print(mylist[0, 1, 3])
print(mylist[0])
print(mylist[1, 1, 3])
doctest.testmod()
