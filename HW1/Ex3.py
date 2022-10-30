import doctest


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
print(
    f"Ex4 solution + picture is in the github and here is the link: https://www.codingame.com/training/easy/blowing-fuse/solution?id=26986264 ")

doctest.testmod(verbose=True)
