liczba = input("Podaj liczbę a ja pokażę pierwszą i ostatnią cyfrę")
print("Pierwsza cyfra: ")
print(liczba[0])
print("Ostatnia cyfra: ")
print(liczba[-1])

odpowiedz = input("Zgadza sie? T/N")

if (odpowiedz == 'T'):
    print("Super")
if (odpowiedz == 'N'):
    print("Nie prawda :)")
