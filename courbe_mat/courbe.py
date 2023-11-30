from matplotlib import pyplot as plt

def tracer_coube(l: list[int]):
    plt.plot(l)
    plt.xlabel("abscisse")
    plt.ylabel("ordonnée")
    plt.title("courbe data")
    plt.show()
