from matplotlib import pyplot as plt

def tracer_histogramme(l: list[int]):
    plt.hist(l, bins=10, color='blue', edgecolor='black')
    plt.xlabel("abscisse")
    plt.ylabel("ordonnée")
    plt.title("histogramme data")
    plt.show()









