import matplotlib.pyplot as plt

def regression_lineaire(x, y):
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

    plt.scatter(x, y, color='blue', label='Données')
    plt.plot(x, d, color='red', label='Droite de régression')
    plt.xlabel('Variable X')
    plt.ylabel('Variable Y')
    plt.legend()
    plt.show()
