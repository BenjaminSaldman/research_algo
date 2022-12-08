import time

import numpy as np
import cvxpy as cp
import random
import sys

MAX_SIZE = sys.maxsize
TRESHOLD = 15


def _generate_eq():
    vars = random.randint(1, TRESHOLD)
    equations = vars
    eq = []
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
    equations = eq_sol[0]  # np.array(eq_sol[0])
    solutions = eq_sol[1]  # np.array(eq_sol[1])
    return np.linalg.solve(equations, solutions)


def cvxpy_solver(eq_sol: tuple):
    A = eq_sol[0]  # np.array(eq_sol[0])
    b = eq_sol[1]  # np.array(eq_sol[1])
    x = cp.Variable(len(b))
    prob = cp.Problem(cp.Minimize(cp.sum(A @ x - b)), [cp.matmul(A, x) == b])
    prob.solve()
    return x.value


def calc_times():
    np_container = {}
    cp_container = {}
    for i in range(15):
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
print(numpy_solver(A))
print(cvxpy_solver(A))
print(calc_times())
