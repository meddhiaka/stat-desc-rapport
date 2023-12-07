def mode(l: list[int]):
    if len(l) >= 20:
        max = l[0]
        for e in l:
            if l.count(e) > max:
                max = l.count(e)
        print(f'Mode: {max}') # afficher la mode
        return max # retourner le mode
    else:
        raise Exception('Il faut que la longeur de la liste soit >= 20')

def medianne(l: list[int]):
    if len(l) >= 20:
        e = sorted(l)
        if len(e) % 2 == 1:
            print(f'medianne: {e[len(e)//2]}')
            return e[len(e)//2]
        else:
            print(f'medianne: {(e[len(e)//2] + e[len(e)//2 - 1])/2}')
            return (e[len(e)//2] + e[len(e)//2 - 1])/2
    else:
        raise Exception('Il faut que la longeur de la liste soit >= 20')

def moyenne(l: list[int]):
    print(f'moyenne: {sum(l)/len(l)}')
    return sum(l)/len(l)

l = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# mode(l) # pour afficher la mode de la liste l
moyenne(l) # afficher la moyenne de la liste
# medianne(l) # afficher le medianne de la liste
