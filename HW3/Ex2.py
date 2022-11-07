import doctest
def lastcall(func=callable, d={}):
    """
    as told us in the first lecture, when you define a data structure with default value it
    will still be mutable. so I defined an empty dictionary that stores the input, and it's computation.

    >>> f(2)
    4
    >>> f(2)
    I already told you that the answer is 4
    >>> y('ABC')
    'ABCABC'
    >>> y('ABC')
    I already told you that the answer is ABCABC
    >>> z((1, 2, 3))
    (1, 2, 3)
    >>> z((1, 2, 3))
    I already told you that the answer is (1, 2, 3)
    """

    def wrapper(*args, **kwargs):

        key = []
        for i in args:
            key.append(i)
        for i in kwargs.items():
            key.append(i)
        key.append(func.__name__)
        key = tuple(key) #convert the given value into a dict.
        if key in d.keys():
            print(f"I already told you that the answer is {d[key]}")
            return
        else:
            d[key] = func(*args, **kwargs)
            return d[key]

    return wrapper


@lastcall
def f(x: int):
    return x ** 2


@lastcall
def y(x: str):
    return x * 2


@lastcall
def z(x: tuple):
    return x



#doctest.testmod()
# f(2)
# f(2)
# y('ABC')
# y('ABC')
# z((1, 2, 3))
# z((1, 2, 3))