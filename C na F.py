# print("Obliczanie stopni Celsjusza na Farenhaita")
# print("°F = (°C * 1.8) + 32")
#
# stopien_c = input("Podaj stopień Celsjusza, który chcesz przeliczyć")
# liczba_1= float(stopien_c)
#
# ulamek = 1.8
# print("Najpierw obliczamy nawias °C * 1.8=")
# print(liczba_1*ulamek)
# mnozenie= liczba_1 * ulamek
# nawias = float(mnozenie)
#
# liczba_2 = 32
# print("Teraz mnożymy nawias ze stałą 32")
# print("Wynik to: ")
# print(nawias+liczba_2)

def cnaf(c):

    liczba_1= float(c)
    return (liczba_1* 1.8) + 32


c = input("Podaj stopień Celsjusza, który chcesz przeliczyć")
print(cnaf(c))

print(cnaf(34))
