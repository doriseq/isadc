print('Sprawdzanie czy liczba jest podzielna przez 3 lub 5 lub 7')
liczba = input("Podaj liczbę")
sprawdzana = float(liczba)
wynik_1 = sprawdzana % 3.0
wynik_2 = sprawdzana % 5.0
wynik_3 = sprawdzana % 7.0
print('Czy dzielona przez 3')
if (wynik_1 == 0):
    print('tak')
else:
    print('nie')

print('Czy dzielona przez 5')
if (wynik_2 == 0):
    print('tak')
else:
    print('nie')

print('Czy dzielona przez 7')
if (wynik_3 == 0):
    print('tak')
else:
    print('nie')
