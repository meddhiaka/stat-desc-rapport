def covariance(x: list[int], y: list[int]):
    if len(x) == len(y) and len(x) >= 20 and len(y) >=20:
        covar = 0
        for i in range(len(x)):
            covar += (x[i] - sum(x) / len(x)) * (y[i] - sum(y) / len(x))
        covar /= len(x)
        print(f'Covariance de x et y: {covar}')
        return covar
    else:
        raise Exception('Il faut que la longeur de les deux liste soit >= 20 aussi égaux')

def correlation(x:list[int], y:list[int]):
    if len(x) == len(y) and len(x) >= 20 and len(y) >=20:
        cov = covariance(x, y) 
        s1 = 0
        s2 = 0
        for e in x:
            s1+= (e-sum(x) / len(x)) ** 2
        for e in y:
            s2+= (e-sum(y) / len(y)) ** 2
        print(f'La correlation de x et y : {cov / (s1 ** 0.5) * (s2 ** 0.5)}')
        return cov / (s1 ** 0.5) * (s2 ** 0.5)
    else:
        raise Exception('Il faut que la longeur de les deux liste soit >= 20 aussi égaux')

    
l1 = [42, 17, 8, 56, 23, 91, 5, 33, 70, 12, 48, 62, 3, 19, 77, 41, 29, 54, 11, 36]
l2 = [9, 45, 27, 68, 14, 72, 50, 6, 38, 83, 20, 95, 2, 64, 30, 51, 16, 78, 22, 57]
# covariance(l1, l2) # Afficher la covariance de l1 et l2
correlation(l1, l2) # Afficher la corrélation de l1 et l2
