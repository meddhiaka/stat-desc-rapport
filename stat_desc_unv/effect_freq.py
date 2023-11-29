def effectifs(l: list[int]):
    res= [] # liste contenant l'effectif de chaque élement
    s= 0 # taille totale d'effectifs
    for e in l:
        res.append({e: l.count(e)})
    for e in res:
        s += list(e.items())[0][1] # l'élement selectionné est l'effectif
    return res, s

def frequences(l: list[dict[int, int]], s:int):
    res= [] # liste contenant la fréquence de chaque élement
    for e in l:
        res.append({list(e.items())[0][0]: list(e.items())[0][1]/s*100})
    return res
    


    
    

