import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import doctest
import math

"""
A. The approximation rate of the 'max_clique' algorithm is $O(|V|/(log|V|)^2)$ apx of maximum clique/independent set
    in the worst case.
    Reference: 
    Boppana, R., & Halldórsson, M. M. (1992).
        Approximating maximum independent sets by excluding subgraphs.
        BIT Numerical Mathematics, 32(2), 180–196. Springer.
        doi:10.1007/BF01994876
    expected
"""

probs = {}
for i in range(2, 12):
    probs[1 / i] = []
n = {np.random.randint(20, 50) for i in range(30)}

exp = []
for i in n:
    exp.append(abs(i - (i / (math.log(i, 2) ** 2))))




def calc():
    """
    >>> G = nx.gnp_random_graph(50, 1)
    >>> len(nx.algorithms.approximation.max_clique(G))
    50
    """
    global probs
    for i in range(2, 12):
        diff = []
        for j in n:
            p = 1 / i
            g = nx.gnp_random_graph(j, p)  # Generating G(n,p) graph
            actual = len(nx.algorithms.approximation.max_clique(g))  # Actual clique size we got from the apx algorithm.
            expected = len(
                sorted(nx.find_cliques(g), key=lambda k: len(k), reverse=True)[0])  # Biggest clique size of g.
            probs[p].append(actual / expected)  # Store the apx ratio.
            diff.append(actual)
        print(np.array(diff) - np.array(exp))


calc()
x = np.array(list(n))
index = 1
for i in probs.keys():
    y = np.array(probs[i])
    plt.subplot(2, 6, index)
    plt.title(f"p ~ {round(i, 2)}", fontsize=10)
    plt.xlabel("n")
    plt.ylabel("apx rate")
    index += 1
    plt.plot(x, y)
plt.subplot(2, 6, index)
plt.show()
doctest.testmod()
# x = np.array([i for i in expected.values()])
# for i in probs.keys():
#     y = np.array(probs[i])
#     print(x-y)
print("We can see that the approximation is much better than the rate that presented in the paper.")
