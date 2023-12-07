def _variance(l: list[int]):
    s1 = 0
    s2 = 0
    for e in l:
        s1 += e
    xb = s1 / len(l)  # xb designe le x bar
    for i in range(len(l)):
        s2 += (l[i] - xb) ** 2
    s2 = s2 / len(l)  # s2 designe le formule final de variance décrit en dessus...
    print(f'variance: {s2}')
    return s2  # cette fonction marche comme fonction et procedure aussi pour simplifier l'affichage

def _ecarttype(variance_value: float):
    print(f'Ecart-type: {variance_value ** 0.5}')
    return variance_value ** 0.5

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
#_variance(l)  # affichage de variance
_ecarttype(_variance(l))  # affichage de l'ecart type
