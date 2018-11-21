def prostokat(a, b)
    return a * b
wartosc_1 = input("Podaj liczbę dla boku A:")
wartosc_2 = input("Podaj liczbę dla boku B: ")

#rzutowanie na liczbę: int(), lub ciąg znaków: str()
liczba_1 = int(wartosc_1)
liczba_2 = int(wartosc_2)
x = '+'
a = '-'
b = '|'
print(x + (a * liczba_1) + x)
bok = a * liczba_1
print((b + (liczba_1 * ' ')+ b))
bok_b = b + (liczba_1 * ' ')+ b
print
print(x + (a * liczba_1) + x)