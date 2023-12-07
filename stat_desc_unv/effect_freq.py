def effectifs(l: list[int]):
    if len(l) >= 20:
        res= [] # liste contenant l'effectif de chaque élement
        s= 0 # taille totale d'effectifs
        for e in l:
            res.append({e: l.count(e)})
        for e in res:
            s += list(e.items())[0][1] # l'élement selectionné est l'effectif
        for k in res:
            print(f'L`effectif de {list(k.items())[0][0]} égale a {list(k.items())[0][1]}')
        return res, s
    else:
        raise Exception('Il faut que la longeur de la liste soit >= 20')

def frequences(l: list[dict[int, int]], s:int):
    if len(l) >= 20:
        res= [] # liste contenant la fréquence de chaqu}e élement
        for e in l:
            res.append({list(e.items())[0][0]: list(e.items())[0][1]/s*100})
        for k in res:
            print(f'La fréquence de {list(k.items())[0][0]} égale a {list(k.items())[0][1]}')
    else:
        raise Exception('Il faut que la longeur de la liste soit >= 20')

l = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
effectifs(l) # pour afficher les effectifs
e = effectifs(l) # e contient les effectifs et leur somme dans un tuple

