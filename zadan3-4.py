wiek = input("Podaj ludzki rok: ")
wiek_int = float(wiek)
rok1 = 10.5
rok2 = 4
if wiek_int <= 2:
    print(wiek_int * rok1 )
else:
    print((rok1 *2) + ((wiek_int - 2) * 4))
