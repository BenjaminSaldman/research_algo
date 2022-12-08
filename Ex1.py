import numpy as np
import cvxpy as cp
import random
import sys

MAX_SIZE = sys.maxsize
TRESHOLD = 5


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
    return eq, solutions


def numpy_solver(eq_sol: tuple):
    equations = np.array(eq_sol[0])
    solutions = np.array(eq_sol[1])
    return np.linalg.solve(equations, solutions)


def cvx_solver(eq_sol: tuple):
    A = np.array(eq_sol[0])
    b = np.array(eq_sol[1])
    x = cp.Variable(len(eq_sol[1]))
    # constraints = [cp.matmul(A, x) == b, x >= 0]
    # objective = cp.Minimize(cp.matmul(A, x) - b)
    prob = cp.Problem(cp.Minimize(cp.sum(A@x)), [cp.matmul(A, x) == b])
    # prob = cp.Problem(objective, constraints)
    prob.solve()
    return x.value


A = _generate_eq()
print(numpy_solver(A))
print(cvx_solver(A))
