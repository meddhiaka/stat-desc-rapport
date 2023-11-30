def variance(l: list[int]):
    s1 = 0
    s2: float = 0
    i = 0
    for e in l:
        s1 += e
    xb = s1 / len(l)
    while i < len(l):
        s2 += (l[i] - xb) ** 2
        i +=1
    s2 = s2 / len(l)
    return s2

def ecartType(e: float):
    return variance(e) ** 0.5

