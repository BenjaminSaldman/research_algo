import doctest


class List(list):

    def __init__(self, *args):
        super().__init__(*args)  # Using parents init method with args

    def __getitem__(self, item):
        """
        >>> List([[[1, 2, 3, 33], [4, 5, 6, 66]],[[7, 8, 9, 99], [10, 11, 12, 122]],[[13, 14, 15, 155], [16, 17, 18, 188]],])[0, 1, 3]
        66
        >>> List([[[1, 2, 3, 33], [4, 5, 6, 66]],[[7, 8, 9, 99], [10, 11, 12, 122]],[[13, 14, 15, 155], [16, 17, 18, 188]],])[0]
        [[1, 2, 3, 33], [4, 5, 6, 66]]
        >>> List([[[1, 2, 3, 33], [4, 5, 6, 66]],[[7, 8, 9, 99], [10, 11, 12, 122]],[[13, 14, 15, 155], [16, 17, 18, 188]],])[1, 1, 3]
        122
        """
        if isinstance(item, tuple):  # to be able to access like n-dimension array.
            ret = super().__getitem__(item[0])  # get the first row that needed.
            for i in item[1:]:  # recursively get inner rows.
                ret = ret[i]

            return ret
        else:
            return super().__getitem__(item)

    def __setitem__(self, key, value):
        if isinstance(key, tuple):
            ret = super().__getitem__(key[0])
            for i in key[1:len(key) - 1]:  # like the method above we find the indexes except the last one.
                ret = ret[i]
            ret.__setitem__(key[len(key) - 1], value)  # changing the value in the specific index we wanted.
            super().__setitem__(key[0], ret)  # insert the modified list to the original one.
        else:
            super().__setitem__(key, value)


mylist = List([
    [[1, 2, 3, 33], [4, 5, 6, 66]],
    [[7, 8, 9, 99], [10, 11, 12, 122]],
    [[13, 14, 15, 155], [16, 17, [18, 188]]],
]
)
# print(mylist)
# print(len(mylist))
# print(mylist[0, 1, 3])
# print(mylist[0])
# print(mylist[1, 1, 3])
# mylist[1, 1, 3] = 7
# print(mylist)
# mylist.append(5)
# print(mylist)
print(mylist[2, 1, 2, 1])
print(mylist[2][1][2][1])
doctest.testmod()
