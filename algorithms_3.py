"""
Author - Benjamin Saldman
Solution for question number 2.
"""

import doctest


def calc_max_player(rights, items, y):
    """
    Function for calculating the number of player with the maximum rights/(f(number of items)+y).
    """
    f = [rights[i] / (items[i] + y) for i in range(len(rights))]
    return f.index(max(f))


def get_available_resource(valuations, resources):
    """
    Returning the available resource according to the valuations of player i.
    It returns the most valuable resource that player i chooses.
    """
    vals = [(valuations[i], i) for i in range(len(valuations))]
    vals = sorted(vals, key=lambda x: x[0], reverse=True)  # Sort the valuations in decreasing order.
    for i in vals:
        if resources[i[1]] != 0:
            return i
    return 0, 0


def weighted_round_robin(rights: list[float], valuations: list[list[float]], y: float):
    """
    The main algorithm, get the rights, valuations of every player and y.
    The function prints how the players should choose the resource and which resource they should choose.

    >>> weighted_round_robin(rights=[1, 2, 4], valuations=[[11, 11, 22, 33, 44], [11, 22, 44, 55, 66], [11, 33, 22, 11, 66]], y=0.5)
    Player number: 2 chooses resource: 4 with value of: 66
    Player number: 1 chooses resource: 3 with value of: 55
    Player number: 2 chooses resource: 1 with value of: 33
    Player number: 0 chooses resource: 2 with value of: 22
    Player number: 2 chooses resource: 0 with value of: 11

    >>> weighted_round_robin(rights=[0, 0, 4], valuations=[[11, 11, 22, 33, 44], [11, 22, 44, 55, 66], [11, 33, 22, 11, 66]], y=0.5)
    Player number: 2 chooses resource: 4 with value of: 66
    Player number: 2 chooses resource: 1 with value of: 33
    Player number: 2 chooses resource: 2 with value of: 22
    Player number: 2 chooses resource: 0 with value of: 11
    Player number: 2 chooses resource: 3 with value of: 11

    >>> weighted_round_robin(rights=[2, 2, 2], valuations=[[11, 11, 22, 33, 44, 78], [11, 22, 44, 55, 66, 45], [11, 33, 22, 11, 66, 12]], y=0.5)
    Player number: 0 chooses resource: 5 with value of: 78
    Player number: 1 chooses resource: 4 with value of: 66
    Player number: 2 chooses resource: 1 with value of: 33
    Player number: 0 chooses resource: 3 with value of: 33
    Player number: 1 chooses resource: 2 with value of: 44
    Player number: 2 chooses resource: 0 with value of: 11

    >>> weighted_round_robin(rights=[2, 2, 2], valuations=[[11, 11, 22, 33, 44, 78], [11, 22, 44, 55, 66, 45], [11, 33, 22, 11, 66, 12]], y=1)
    Player number: 0 chooses resource: 5 with value of: 78
    Player number: 1 chooses resource: 4 with value of: 66
    Player number: 2 chooses resource: 1 with value of: 33
    Player number: 0 chooses resource: 3 with value of: 33
    Player number: 1 chooses resource: 2 with value of: 44
    Player number: 2 chooses resource: 0 with value of: 11

    >>> weighted_round_robin(rights=[2, 2, 2], valuations=[[11, 11, 11, 11, 11, 11], [11, 11, 11, 11, 11, 11], [11, 11, 11, 11, 11, 11]], y=0.5)
    Player number: 0 chooses resource: 0 with value of: 11
    Player number: 1 chooses resource: 1 with value of: 11
    Player number: 2 chooses resource: 2 with value of: 11
    Player number: 0 chooses resource: 3 with value of: 11
    Player number: 1 chooses resource: 4 with value of: 11
    Player number: 2 chooses resource: 5 with value of: 11

    >>> weighted_round_robin(rights=[1, 2, 4], valuations=[[11, 11, 11, 11, 11, 11], [11, 11, 11, 11, 11, 11], [11, 11, 11, 11, 11, 11]], y=0.5)
    Player number: 2 chooses resource: 0 with value of: 11
    Player number: 1 chooses resource: 1 with value of: 11
    Player number: 2 chooses resource: 2 with value of: 11
    Player number: 0 chooses resource: 3 with value of: 11
    Player number: 2 chooses resource: 4 with value of: 11
    Player number: 1 chooses resource: 5 with value of: 11

    """
    num_of_players = len(rights)  # Total number of players
    num_of_resources = len(valuations[0])  # Number of resources.
    items = [0 for i in
             range(num_of_players)]  # Number of items that player i got. First, none of them getting an item.
    resources = [1 for i in range(
        num_of_resources)]  # Number of available resources. If resources[i]=1, then the resource is available.
    while sum(resources) != 0:  # While there is an available resource.
        max_player = calc_max_player(rights, items, y)  # Getting the index of the player with max(rights/(f(s)+y)
        items[max_player] += 1  # Increasing the number of items of player i0
        value, num_of_resource = get_available_resource(valuations[max_player],
                                                        resources)  # Getting the available items according to the valuations of player i.
        resources[num_of_resource] = 0  # Deleting the resource that was given.
        print(f'Player number: {max_player} chooses resource: {num_of_resource} with value of: {value}')


