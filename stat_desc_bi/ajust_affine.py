import matplotlib.pyplot as plt

def ajustement_affine_bivarie(x: list[int], y:list[int]):
    if len(x) == len(y) and len(x) >= 20 and len(y) >=20:
        i = 0
        denum = 0
        num = 0
        while i < len(x):
            num += (x[i] - sum(x) / len(x)) * (y[i] - sum(y) / len(y))
            i+=1

        for e in x:
            denum += (e - sum(x) / len(x))**2
        

        a = num / denum
        b = sum(y) / len(y) - a * sum(x) / len(x)

        max = x[0]
        min = x[0]
        for e in x:
            if e > max:
                max = e
            if e < min:
                min = e

        x_ = [max, min]
        y_ = []
        for e in x_:
            y_.append(a * e + b)

        plt.scatter(x, y, label='Données')
        plt.plot(x_, y_, color='red', label=f'Ajustement affine: y = {a:.2f}x + {b:.2f}')
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title('Ajustement Affine d\'une Série Statistique Bivariée')
        plt.legend()
        plt.show()
    else:
        raise Exception('Il faut que la longeur de les deux liste soit >= 20 aussi égaux')

l1 = [42, 17, 8, 56, 23, 91, 5, 33, 70, 12, 48, 62, 3, 19, 77, 41, 29, 54, 11, 36]
l2 = [9, 45, 27, 68, 14, 72, 50, 6, 38, 83, 20, 95, 2, 64, 30, 51, 16, 78, 22, 57]
ajustement_affine_bivarie(l1, l2)
