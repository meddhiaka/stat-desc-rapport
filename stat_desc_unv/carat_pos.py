def mode(l: list[int]):
    for e in l:
        if l.count(e) > max:
            max = l.count(e)
    return max

def medianne(l: list[int]):
    e = sorted(l)
    if len(e) % 2 == 1:
        return e[len(e)//2]
    else:
        return (e[len(e)//2] + e[len(e)//2 - 1])/2

def moyenne(l: list[int]):
    return sum(l)/len(l)