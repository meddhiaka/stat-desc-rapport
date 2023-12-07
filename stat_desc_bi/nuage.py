from matplotlib import pyplot as plt

def nuagePoints(l1: list[int], l2: list[int]):
    if(len(l1)>= 20 and len(l2) >= 20 and len(l2) == len(l1)):
        plt.scatter(l1, l2)
        plt.xlabel("l1")
        plt.ylabel("l2")
        plt.title("Nuage de points")
        plt.show()
    else:
        raise Exception('Il faut que la longeur de la liste soit >= 20')

l1 = [42, 17, 8, 56, 23, 91, 5, 33, 70, 12, 48, 62, 3, 19, 77, 41, 29, 54, 11, 36]
l2 = [9, 45, 27, 68, 14, 72, 50, 6, 38, 83, 20, 95, 2, 64, 30, 51, 16, 78, 22, 57]
nuagePoints(l1, l2)

