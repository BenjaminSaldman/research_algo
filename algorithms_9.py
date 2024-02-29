import cvxpy
import functools
import numpy as np
import doctest


def find_decomposition(budget: list[float], preferences: list[set[int]]):
    """
    This function gets a budget and preferences and prints a decompose of
    the budget if and only if the budget is decomposable. Otherwise, it returns False.

    >>> find_decomposition(budget=[400, 50, 50, 0], preferences=[{0, 1}, {0, 2}, {0, 3}, {1, 2}, {0}])
    Player 0 should donate: 100.0 to issue 0
    Player 1 should donate: 100.0 to issue 0
    Player 2 should donate: 100.0 to issue 0
    Player 3 should donate: 50.0 to issue 1, 50.0 to issue 2
    Player 4 should donate: 100.0 to issue 0

    >>> find_decomposition(budget=[400, 50, 50, 0], preferences=[{0, 1}, {0, 2}, {0, 3}, {0, 2}, {0}])
    Player 0 should donate: 50.0 to issue 0, 50.0 to issue 1
    Player 1 should donate: 75.0 to issue 0, 25.0 to issue 2
    Player 2 should donate: 100.0 to issue 0
    Player 3 should donate: 75.0 to issue 0, 25.0 to issue 2
    Player 4 should donate: 100.0 to issue 0

    >>> find_decomposition(budget=[0, 50, 50, 0], preferences=[{0, 1}, {0, 2}, {0, 3}, {1, 2}, {0}])
    False
    """
    donations = budget  # Change the name of the input, for the use of the function.
    C = sum(donations)  # C = d_1 + ... + d_m.
    n = len(preferences)  # n = number of players.
    vars = [[] for j in range(len(donations))]  # Vars for every issue.
    allocations = []  # Total list of the vars.
    alloc_for_player = [[] for j in range(n)]  # Vars that assigned for each player - d_{i,j}.
    for i in range(n):
        for j in preferences[i]:
            x = cvxpy.Variable()  # Create d_{i,j}.
            vars[j].append(x)  # Add it to the issue j.
            allocations.append(x)  # Add it to the total list.
            alloc_for_player[i].append(x)  # Add it to the list of player i.

    positivity_constraints = [v >= 0 for v in allocations]  # Actually, v>0 only if u_{i,j}>1, so it's the same.
    sum_for_issue_constraints = [sum(vars[j]) == donations[j] for j in range(len(donations))]  # Sum[i] d_{i,j} = d_j.
    sum_for_participant_constraints = [sum(alloc_for_player[j]) == C / n for j in range(n)]  # Sum[j] C/n = d_j.
    # We actually need to satisfy only the constraints, so the objective should be a dummy.
    problem = cvxpy.Problem(cvxpy.Maximize(0),
                            constraints=positivity_constraints + sum_for_issue_constraints + sum_for_participant_constraints)
    problem.solve(solver=cvxpy.CVXOPT)  # Solve the problem using CVXOPT.
    if problem.status != "optimal":
        return False  # If no solution exists, return false.
    for i in range(n):
        msg = f"Player {i} should donate: "
        idx = 0
        for j in preferences[i]:
            t = np.round(alloc_for_player[i][idx].value)  # t = d_{i,j}.
            if t > 0:
                msg += f"{t} to issue {j}, "
            idx += 1
        print(msg[:len(msg) - 2])


if __name__ == '__main__':
    doctest.testmod(verbose=True)
