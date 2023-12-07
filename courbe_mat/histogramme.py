from matplotlib import pyplot as plt

def tracer_histogramme(l: list[int]):
    if len(l) >= 20:
        plt.hist(l, bins=10, color='blue', edgecolor='black')
        plt.xlabel("abscisse")
        plt.ylabel("ordonnée")
        plt.title("histogramme data")
        plt.show()
    else:
        raise Exception('Il faut que la longeur de la liste soit >= 20')


l = [42, 17, 8, 56, 23, 91, 5, 33, 70, 12, 48, 62, 3, 19, 77, 41, 29, 54, 11, 36]
tracer_histogramme(l)





