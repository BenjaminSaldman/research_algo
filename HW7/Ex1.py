import time

import numpy as np
import cvxpy as cp
import matplotlib.pyplot as plt
import random
import sys
import doctest

MAX_SIZE = sys.maxsize
TRESHOLD = 15


def _generate_eq():
    """
    System of linear equations generator.
    """
    vars = random.randint(1, TRESHOLD)  # Number of variables.
    equations = vars  # Number of equations.
    eq = []  # Equations.
    solutions = []
    for i in range(equations):
        temp = []
        for j in range(vars):
            temp.append(random.randint(0, TRESHOLD))
        solutions.append(random.randint(0, TRESHOLD))
        eq.append(temp)
    eq = np.array(eq)
    solutions = np.array(solutions)
    if np.linalg.det(eq) == 0:  # Singular matrix
        return _generate_eq()
    return eq, solutions


def numpy_solver(eq_sol: tuple):
    """
    Solving the system of linear equations using numpy.linalg.
    >>> numpy_solver((np.array([[4, 4, 3],[3, 1, 1],[1, 4, 2]]), np.array([3, 0, 1])))
    array([-1., -2.,  5.])
    >>> numpy_solver((np.array([[1]]), np.array([1])))
    array([1.])
    """
    equations = eq_sol[0]
    solutions = eq_sol[1]
    return np.linalg.solve(equations, solutions)


def cvxpy_solver(eq_sol: tuple):
    """
    Solving the system of linear equations using cvxpy.
    >>> cvxpy_solver((np.array([[4, 4, 3],[3, 1, 1],[1, 4, 2]]), np.array([3, 0, 1])))
    array([-1., -2.,  5.])
    >>> cvxpy_solver((np.array([[1]]), np.array([1])))
    array([1.])
    """
    A = eq_sol[0]
    b = eq_sol[1]
    x = cp.Variable(len(b))
    prob = cp.Problem(cp.Minimize(cp.sum(A @ x - b)), [cp.matmul(A, x) == b])
    prob.solve()
    return x.value


def calc_times():
    np_container = {}
    cp_container = {}
    for i in range(50):
        A = _generate_eq()
        t1 = time.time()
        numpy_solver(A)
        t2 = time.time() - t1
        np_container[len(A[0]) ** 2] = t2
        t1 = time.time()
        cvxpy_solver(A)
        t2 = time.time() - t1
        cp_container[len(A[0]) ** 2] = t2
    return np_container, cp_container


A = _generate_eq()
print(A)
print(numpy_solver(A))
print(cvxpy_solver(A))
print(calc_times())
np_container, cp_container = calc_times()
x1 = list(i for i in np_container.keys())
y1 = list(i for i in np_container.values())
x2 = list(i for i in cp_container.keys())
y2 = list(i for i in cp_container.values())
plt.plot(x2, y2, 'r', label="Cvxpy")
plt.plot(x1, y1, 'b', label="Numpy")
plt.title("Numpy vs Cvxpy")
plt.xlabel("Matrix size")
plt.ylabel("Time in seconds")
plt.legend(loc="upper left")
plt.show()
print("We can conclude that numpy runs much faster than Cvxpy")
