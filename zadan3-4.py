# wiek = input("Podaj ludzki rok: ")
# wiek_int = float(wiek)
# rok1 = 10.5
# rok2 = 4
# if wiek_int <= 2:
#     print(wiek_int * rok1 )
# else:
#     print((rok1 *2) + ((wiek_int - 2) * 4))



def rok_psa(wiek):
    wiek_int = int(wiek)
    rok1 = 10.5
    if wiek_int <= 2:
        print(wiek_int * rok1)
    else:
        print((rok1 * 2) + ((wiek_int - 2) * 4))


while True:
    try:
        wiek = input("Podaj ludzki rok: ")
        rok_psa(wiek)
        break
    except ValueError:
        print("Podales zla wartosc! Sprobuj jeszcze raz")
