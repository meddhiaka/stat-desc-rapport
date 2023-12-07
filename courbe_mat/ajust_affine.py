import matplotlib.pyplot as plt

def regression_lineaire(x, y):
    if len(x) >= 20 and len(y) >=20 and len(y) == len(x) :
        s1 = 0
        s2 = 0
        for i in range(len(x)):
            s1 += (x[i] - sum(x) / len(x)) * (y[i] - sum(y) / len(x))
        for i in range(len(x)):
            s2 += (x[i] - sum(x) / len(x)) ** 2
        
        a = s1 / s2
        b = sum(y) / len(x) - a * sum(x) / len(x)

        d = []
        for xi in x:
            d.append(a* xi + b)
        
        print(f'a: {a}, b: {b}')

        plt.scatter(x, y, color='blue', label='Données')
        plt.plot(x, d, color='red', label='Droite de régression')
        plt.xlabel('Variable X')
        plt.ylabel('Variable Y')
        plt.legend()
        plt.show()
    else:
        raise Exception('Il faut que la longeur de les deux liste soit >= 20 aussi égaux')



l = [42, 17, 8, 56, 23, 91, 5, 33, 70, 12, 48, 62, 3, 19, 77, 41, 29, 54, 11, 36]
l2 = [9, 45, 27, 68, 14, 72, 50, 6, 38, 83, 20, 95, 2, 64, 30, 51, 16, 78, 22, 57]
regression_lineaire(l, l2) # Droite de regression