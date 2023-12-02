from . import effect_freq
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

res = int(input("Choisir 1 pour calculer les effectifs sinon 2 pour les fréquences: "))

print("#############################################")
if res == 1:
    print("Testing mode1: Effectifs of a serie:")
    print("Chaque effectif est une liste de deux elements: [valeur, effectif]:")
    print(effectifs[0])
    print(f"\nLa somme des effectifs est egale a la taille de la serie: {effectifs[1]}")
    sys.exit()
else:
    print("Testing mode2: Frequencies of a serie")
    frequences = effect_freq.frequences(effectifs[0], effectifs[1])
    print("Chaque frequence est une liste de deux elements: [valeur, frequence en %]:")
    print(frequences)
    sys.exit()