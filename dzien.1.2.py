imie = input("Jak masz na imię")
imie = imie.strip(' ')
dlugosc_imienia = (len(imie))
ostatnia_litera_imienia = imie[-1]
print("Cześć")

print(imie.upper())
if ((imie[-1])=='a'):
    print(jesteś kobietą)
print("Twoje imię ma: " + str(dlugosc_imienia) + " liter")
print("Twoja ostatnia litera to " + ostatnia_litera_imienia)

