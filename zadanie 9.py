print('sprawdzanie czy liczba jest podzielne przez 3 i 5 i 7')
liczba = input('Podaj liczbę')
sprawdzana = float(liczba)
wynik_1 = sprawdzana % 3.0
wynik_2 = sprawdzana % 5.0
wynik_3 = sprawdzana % 7.0

if (wynik_1 == 0 and wynik_2 == 0 and wynik_3 == 0):
    print('tak')
else:
    print('nie')
