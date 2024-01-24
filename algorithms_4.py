import cvxpy
import doctest
import cvxopt
import matplotlib.pyplot as plt
import time

'''
  In order to make the program run, please make sure you installed the package CVXOPT which
  contains a solver for integer programming problems.
'''


def egalitarian_allocation(valuations: list[list[float]]):
    """
    I used the solution code of ex3 question 1.


    >>> egalitarian_allocation(valuations=[[11, 11, 22, 33, 44], [11, 22, 44, 55, 66], [11, 33, 22, 11, 66]])
    Player 0 gets items 0, 4 with value 55
    Player 1 gets items 3 with value 55
    Player 2 gets items 1, 2 with value 55

    >>> egalitarian_allocation(valuations=[[11, 11, 11, 11, 11], [11, 11, 11, 11, 11], [11, 11, 11, 11, 11]])
    Player 0 gets items 1, 2 with value 22
    Player 1 gets items 4 with value 11
    Player 2 gets items 0, 3 with value 22

    >>> egalitarian_allocation(valuations=[[11, 11, 11, 11, 11,11], [11, 11, 11, 11, 11,11], [11, 11, 11, 11, 11,11]])
    Player 0 gets items 1, 3 with value 22
    Player 1 gets items 0, 2 with value 22
    Player 2 gets items 4, 5 with value 22
    """
    # Declare the variables and utility
    num_of_players = len(valuations)
    num_of_resources = len(valuations[0])
    variables = []
    utility_for_player = []

    # Calculation of the utility for all player
    for i in range(num_of_players):
        utility = 0
        for j in range(num_of_resources):
            variables.append(cvxpy.Variable(num_of_players,
                                            integer=True))  # Make each variable an integer (because it is an integer programming program).
            utility += variables[j][i] * valuations[i][j]  # Calculation of the utility for player i
        utility_for_player.append(utility)  # insert  utility for player i to utility list

    min_utility = cvxpy.Variable(integer=True)

    '''
    List all the constraints for the maximize function.
    We need that every variable will be positive, we need to maximize the minimum utility for every player and we need that
    from every variable, only 1 will get the resource, so we need that the sum will be 1.
    '''
    fixed_constraints = \
        [variables[i][j] >= 0 for i in range(num_of_resources) for j in range(num_of_players)] + \
        [utility_for_player[i] >= min_utility for i in range(num_of_players)] + \
        [sum(variables[i]) == 1 for i in range(num_of_resources)]

    # Solve the equation under the provided constraints.
    prob = cvxpy.Problem(cvxpy.Maximize(min_utility), constraints=fixed_constraints)
    prob.solve()

    # Print the result.
    for i in range(num_of_players):
        resources = ""
        value = 0
        for j in range(num_of_resources):
            if variables[j][i].value == 1:
                resources += str(j) + ", "
                value += valuations[i][j]

        print(f"Player {i} gets items {resources[:len(resources) - 2]} with value {value}")


# Code of roy, question 1 ex3.
def egalitarian_allocation_linear(valuations: list[list[float]]):
    # Declare the variables and utility
    num_of_players = len(valuations)
    num_of_resources = len(valuations[0])
    variables = []
    utility_for_player = []

    # Calculation of the utility for all player
    for i in range(num_of_players):
        utility = 0
        for j in range(num_of_resources):
            variables.append(cvxpy.Variable(num_of_players))  # fractions of all the resources by number of player
            utility += variables[j][i] * valuations[i][j]  # Calculation of the utility for player i
        utility_for_player.append(utility)  # insert  utility for player i to utility list

    min_utility = cvxpy.Variable()

    # list all the constraints for the maximize function
    fixed_constraints = \
        [variables[i][j] >= 0 for i in range(num_of_resources) for j in range(num_of_players)] + \
        [variables[i][j] <= 1 for i in range(num_of_resources) for j in range(num_of_players)] + \
        [utility_for_player[i] >= min_utility for i in range(num_of_players)] + \
        [sum(variables[i]) == 1 for i in range(num_of_resources)]

    # solve the equation
    prob = cvxpy.Problem(cvxpy.Maximize(min_utility), constraints=fixed_constraints)
    prob.solve(solver=cvxpy.ECOS)

    # print the result
    for i in range(num_of_players):
        print(f"player {i} receives ", end=" ")
        for j in range(num_of_resources):
            if j == 0:
                print(f"{abs(round(variables[j][i].value * 100, 2))}% of resource {j}", end="")
            else:
                print(f" and {abs(round(variables[j][i].value * 100, 2))}% of resource {j}", end="")
        print()


def compare_running_time():
    """
    Program for comparing the running time between the integer programming to the linear programming.
    """
    integer = []  # Values of time and number of items for the integer program.
    linear = []  # Values of time and number of items for the linear program.
    for i in range(5, 16):
        # Calculating the overall time for each program with 2 players and items of size {5,...,15}.
        start = time.time()
        egalitarian_allocation_linear([[11 for j in range(i)], [11 for j in range(i)]])
        end = time.time()
        linear.append((i, end - start))
        start = time.time()
        egalitarian_allocation([[11 for j in range(i)], [11 for j in range(i)]])
        end = time.time()
        integer.append((i, end - start))
    # Plotting the results.
    plt.plot([i[0] for i in integer], [i[1] for i in integer])
    plt.xlabel('Number of items')
    plt.ylabel('Running time')
    plt.title('Integer programming')
    plt.show()
    plt.plot([i[0] for i in linear], [i[1] for i in linear])
    plt.xlabel('Number of items')
    plt.ylabel('Running time')
    plt.title('Linear programming')
    plt.show()


if __name__ == "__main__":
    # Run this function if you want to get the plots of the running times.
    compare_running_time()
    doctest.testmod(verbose=True)
