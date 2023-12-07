from . import effect_freq, carat_pos, var_ecart
import sys

serie = input("Enter the elements sparated by spaces: ").split()
effectifs = effect_freq.effectifs(serie)
i = 0
while i < len(serie):
    serie[i] = int(serie[i])
    i+=1

try:
    if len(serie) < 20:
        raise Exception("20 comme longeur minimal de la serie statistique!")
except Exception as e:
    print(e)

print(f"INPUT: {serie} comme liste\n\n")
str = "Choisir \n \t* 1 pour calculer les effectifs \n\t* 2 donner les fréquences \n\t* 3 donner la variance et l'écar-type\n\t* Donner la mode, medianne et la moyenne \n"
res = int(input(str))

print("#############################################")

while True:
    if res == 1:
        print("Testing mode1: Effectifs of a serie:")
        print("Chaque effectif est une liste de deux elements: [valeur, effectif]:")
        print(effectifs[0])
        print(f"\nLa somme des effectifs est egale a la taille de la serie: {effectifs[1]}")
        sys.exit()
        break
    elif  res == 2:
        print("Testing mode2: Frequencies of a serie")
        frequences = effect_freq.frequences(effectifs[0], effectifs[1])
        print("Chaque frequence est une liste de deux elements: [valeur, frequence en %]:")
        print(frequences)
        sys.exit()
        break
    elif res == 3:
        print("Testing mode3: Variance et écart-type")
        var = var_ecart.ecartType(serie)
        ecart = var_ecart.variance(serie)
        print(f"\n\tVariance de la série: {var}\n\tL'écartype de la série: {ecart}\n")
        sys.exit()
        break
    elif res == 4:
        print("Testing mode4: Mode, medianne et moyenne")
        print(f"\n\tMoyenne de la serie: {carat_pos.moyenne(serie)} \n\tMedianne de la serie: {carat_pos.medianne(serie)} \n\t Mode de la serie: {carat_pos.mode(serie)} ")
        sys.exit()
        break
    else:
        print("Essayer une autre fois,")
        res = input(str)
