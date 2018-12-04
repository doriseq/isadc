#
# """
# 1. otwórz plik z danymi dane.txt
# 2. przeiteruj kazdy znak w danych wejsciowych
# 3. policz ilość znaku bazowego w tekście (a.b.c.d...)
# 4. zwiększ licznik dla danego znaku
# 5. zapisz liczniki do pickle
# """
import string
from dzien3 import policz_litere


def otworz_plik(plik):
    plik = 'cwicz.txt' #input("Podaj nazwę pliku: ")
    try:
        with open(plik) as dane:
            return dane.read()
    except:
        print("Coś z tym plikiem jest nie tak")
        otworz_plik()


def zapisz_plik(dane):
    plik= 'wyniki.txt'
    try:
        with open(plik, 'rb+') as wyniki_plik:
            pickle.dump(dane, wyniki_plik)
    except Exception as e:
        print(e)
        print("coś z tym plikiem jest nie tak")

znaki = string.ascii_letters
dane = otworz_plik('cwicz.txt')
print(dane)

dlugosc = len(dane)
stats = {'dlugosc': dlugosc}

for i in znaki:
    ilosc = dane.count(i)
    stats[i] = ilosc

print(stats)
zapisz_plik(stats)

with open('wyniki.txt', 'rb+') as wyniki_plik:
    print(pickle.load(wyniki_plik))