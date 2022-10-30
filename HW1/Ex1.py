import doctest


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
doctest.testmod(verbose=True)
