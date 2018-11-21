wartosc_1 = input("Podaj liczbę dla szerokości:")
wartosc_2 = input("Podaj liczbę dla wysokości: ")

#rzutowanie na liczbę: int(), lub ciąg znaków: str()
liczba_1 = int(wartosc_1)
liczba_2 = int(wartosc_2)
x = '+'
a = '-'
b = '|'
print(x + (a * liczba_1) + x)
bok = a * liczba_1
print(('|' + (liczba_1 * ' ')+ '|\n')) * wartosc_2
print(x + (a * liczba_1) + x)
