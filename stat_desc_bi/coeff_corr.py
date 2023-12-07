def correlation_coefficient(x: list[int], y:list[int]):
    if len(x) == len(y) and len(x) >= 20 and len(y) >=20:
        denomx = 0
        denomy = 0
        num = 0

        i = 0
        while i < len(x):
            denomx += (x[i] - sum(x) / len(x))**2
            denomy += (y[i] - sum(y) / len(y))**2
            i+=1

        i = 0
        while i < len(x):
            num += (x[i] - sum(x) / len(x)) * (y[i]- sum(y) / len(y))
            i+=1
        

        denomx = denomx ** 0.5
        denomy = denomy ** 0.5 

        cor = num / (denomx * denomy)
        
        print(f'Coefficient de correlation d`une serie statistique bivarie: {cor:.2f}')
        return cor
    else:
        raise Exception('Il faut que la longeur de les deux liste soit >= 20 aussi égaux')


l1 = [42, 17, 8, 56, 23, 91, 5, 33, 70, 12, 48, 62, 3, 19, 77, 41, 29, 54, 11, 36]
l2 = [9, 45, 27, 68, 14, 72, 50, 6, 38, 83, 20, 95, 2, 64, 30, 51, 16, 78, 22, 57]
correlation_coefficient(l1, l2) # fonction pour afficher la correlation d'une serie statistique bivariée