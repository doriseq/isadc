# wartosc_1 = input("Podaj liczbę dla szerokości:")
# wartosc_2 = input("Podaj liczbę dla wysokości: ")
# #rzutowanie na liczbę: int(), lub ciąg znaków: str()
# a = int(wartosc_1)
# b = int(wartosc_2)
#
# print('+' + ('-' * a) + '+')
# print((('|' + (' ' * a) + '|\n') * b), end='')
# print('+' + ('-' * a) + '+')

def prostokat(a, b):
    wartosc_1 = input("Podaj liczbę dla szerokości:")
    wartosc_2 = input("Podaj liczbę dla wysokości: ")
    a = int(wartosc_1)
    b = int(wartosc_2)

    gora_dol = '+' + ('-' * a) + '+'
    srodek = '|' + (' ' * a) + "|\n"
    return (gora_dol + '\n' + srodek *b + gora_dol)


print(prostokat(4,5))
