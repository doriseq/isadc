# slownik = {"imie": ['Łukasz', 'Ala', 'Ola'],
#            "nazwiska": ['Falkowicz', 'Kowalska', 'Malinowska']
# }
# miasta = {'miasta': ['Warszawa', 'Gdańsk', 'Sopot', 'Kraków']}
#
# slownik.update(miasta)
#
# # print(type(slownik))
# # print(slownik)
# # print(slownik.keys())
# # print(slownik.items())
#
#
# for index, imie in enumerate(slownik["imie"]):
#     nazwisko = slownik["nazwiska"][index]
#     miasto = slownik["miasta"][index]
#     print("Mam na imię: {} nazwisko {} i mieszkam w {}". format(imie, nazwisko, miasto))
#
# # def wyswietl_slownik():
# #     for index, imie in enumerate(slownik["imie"]):
# #         nazwisko = slownik["nazwiska"][index]
# #         miasto = slownik["miasta"][index]
# #         print("Mam na imię: {} nazwisko {} i mieszkam w {}". format(imie, nazwisko, miasto))
#
# # for klucz, wartosc in slownik.items():
# #     print(klucz)
# #     for dana in nazwiska:
# #     print(dana)

# plik = open('dane.txt', 'w+')
# print(plik.readline(), end='')
# plik.seek(2)
# print(plik.readline(), end='')
# print(plik.readline(), end='')

# plik.write('A')
# print(plik.readline(), end='')
# plik.seek(0)
# plik.close()
#
# plik = open('dane.txt', 'r+')
# licznik = int(plik.readline())
# licznik = licznik + 1
# print(licznik)
# plik.seek(0)
# plik.write(str(licznik)) #5
# plik.close()
#
# with open('dane.txt', 'r+') as plik:
#     licznik = int(plik.readline())
#     licznik = licznik + 1
#     print(licznik)
#     plik.seek(0)
#     plik.write(str(licznik)) #5
#
imie = input("Jak masz na imię?")
tresc = input("Co się dziś wydarzyło?")
with open('dzien.txt', 'a+') as plik:
    plik.write(imie + ':' + tresc + ':' + '\n')
    print(plik)


