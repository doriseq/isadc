



#
# liczby = range(0,50,2)
# for liczba in liczby:
#     if (liczba %2 == 0):
#         print(liczba)

# liczby = range(0,50)
# for liczba in liczby:
#     if (liczba %2 != 0):
#         continue
#     print(liczba)
#
# liczby = range(0,50)
# for liczba in liczby:
#     if (liczba %2 != 0):
#         break
#     print(liczba)
# print('koniec')
#
# liczby = range(0,51,2)
# for liczba in liczby:
#         print(liczba)
#
# napis = 'Ala ma kota'
# for i in napis:
#     print(i)
#
# lista_imion = ['Ola', 'Ala' , 'Tomek', 'Jan']
# for imie in(lista_imion):
#     print(imie)
#
# lista_imion = ['Ola', 'Ala' , 'Tomek', 'Jan']
# for i, imie in enumerate(lista_imion):
#     print('Na pozycji: {} jest imie: {}'. format(i, imie))
#
#
# lista_nazwiska = ['Kowalska', 'Malinowska', 'Iksiński', 'Igrekowski']
# for imie, nazwisko in zip(lista_imion, lista_nazwiska):
#     print('Imię i nazwisko: {} {}'. format(imie, nazwisko))
#
# lista = ['aaa', 'bbb', 'ccc', 'ddd']
# przypisanie = lista
#
#
# lista[0] = 'xxx'
# przypisanie[1] = 'www'
# print(lista)
# print(przypisanie)
#
# import copy #nazwa biblioteki
#
# lista = ['aaa', 'bbb', 'ccc', 'ddd']
# przypisanie = lista
#
# kopia_indeksami= lista[:]
# kopia_konstruktorem= list(lista)
# kopia_metoda = lista.copy()
# kopia_biblioteka = copy.copy(lista)
#
# print(lista)
# print(przypisanie)
# print(kopia_indeksami)
# print(kopia_konstruktorem)
# print(kopia_metoda)
# print(kopia_biblioteka)


def policz_litere():
    litera = 'a'
    tekst = "Ala ma kota"
    return tekst.count(litera)
print(policz_litere())

def policz_litere(litera = 'a', tekst = 'Ala ma kota'):
    litera = litera.lower()
    tekst = tekst.lower()
    return tekst.count(litera)
print(policz_litere())

