print("Sprawdż czy liczba jest parzysta")
liczba = input("Podaj liczbę")
sprawdzana=float(liczba)
wynik = sprawdzana % 2
if (wynik == 0 ):
    print("tak")
if (wynik != 0 ):
    print('nie')
