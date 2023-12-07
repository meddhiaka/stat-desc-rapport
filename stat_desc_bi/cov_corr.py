def covariance(x: list[int], y: list[int]):
    if len(x) == len(y):
        covar = 0
        for i in range(len(x)):
            covar += (x[i] - sum(x) / len(x)) * (y[i] - sum(y) / len(x))
        covar /= len(x)
    else:
        return -1
    return covar

def correlation(x:list[int], y:list[int]):
    if len(x) == len(y):
        cov = covariance(x, y) 
        s1 = 0
        s2 = 0
        for e in x:
            s1+= (e-sum(x) / len(x)) ** 2
        for e in y:
            s2+= (e-sum(y) / len(y)) ** 2
        return cov / (s1 ** 0.5) * (s2 ** 0.5)
    else:
        return -1