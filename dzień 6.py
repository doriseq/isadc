#
# zmienna_globalna = 'A'
#
# def rodzic():
#     zmienna_lokalna = 'B'
#     global zmienna_globalna
#
#     zmienna_globalna = 'A zmienione'
#     print("Funkcja rodzic: " + zmienna_globalna)
#     print("Funkcja rodzic: " + zmienna_lokalna)
#
#
# print(zmienna_globalna)
#
# rodzic()
#
# print(zmienna_globalna)
# # print(zmienna_lokalna)

# from moduly import przywitanie as moje_przywitanie
# # import dzien3
# #
# # moje_przywitanie.czesc("Łukasz")
# #
# # ilosc = dzien3.policz_litere('b', 'baran baranowy')
# # print(ilosc)


def otworz_plik(plik):
    with open(plik) as dane:
        return dane.read()
return otworz_plik()
print(otworz_plik())
