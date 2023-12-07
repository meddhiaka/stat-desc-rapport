from matplotlib import pyplot as plt

def tracer_coube(l: list[int]):
    if len(l) >= 20:
        plt.plot(l)
        plt.xlabel("abscisse")
        plt.ylabel("ordonnée")
        plt.title("courbe data")
        plt.show()
    else:
        raise Exception('Il faut que la longeur de la liste soit >= 20')

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
tracer_coube(l)