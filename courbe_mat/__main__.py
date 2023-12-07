from . import courbe, histogramme, ajust_affine
import sys

serie = input("Enter the elements sparated by spaces: ").split()
serie2 = input("Enter the elements sparated by spaces: ").split()
i=0
while i < len(serie):
    serie[i] = int(serie[i])
    serie2[i] = int(serie2[i])
    i+=1

try:
    if ((len(serie)<20) and (len(serie2) < 20)):
        raise Exception("20 comme longeur minimal pour les deux listes")
except Exception as e:
    print(e)

print(f"INPUT: {serie} comme liste\n\n")

res = int(input("Choisir 1 pour la graphe sinon 2 pour le histogramme :"))

print("#############################################")
while True:
    if res == 1:
        print("Testing mode1: Courbe: ")
        courbe.tracer_coube(serie)
        sys.exit()
        break
    elif res == 2:
        print("Testing mode2: Histogramme: ")
        histogramme.tracer_histogramme(serie)
        sys.exit()
        break
    elif res == 3:
        print("Testing mode3: Ajustement affine: ")
        ajust_affine.droitRegression(serie, serie2)
        break
    else:
        res = int(input("Choisir 1 pour la graphe sinon 2 pour le histogramme :"))
