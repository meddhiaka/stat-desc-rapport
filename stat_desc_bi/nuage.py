from matplotlib import pyplot as plt

def nuagePoints(l1: list[int], l2: list[int]):
    plt.scatter(l1, l2)
    plt.xlabel("l1")
    plt.ylabel("l2")
    plt.title("Nuage de points")
    plt.show()