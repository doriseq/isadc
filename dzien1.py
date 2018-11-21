imie = input("Jak masz na imię?")
imie = imie.strip(' ')
dlugosc_imienia: int=(len(imie))
ostatnia_litera_imienia = imie[-1]
print("Cześć")
print(imie)
pochodzenie = input("Skąd pochodzisz?")
print("super, ja też")
if((imie[-1])=='a'):
    print("jesteś kobietą")
if((imie[-1] != 'a')):
    print("jestes mężczyczną")

print("Twoje imię ma: " + str(dlugosc_imienia) + " liter")
print("Twoja ostatnia litera to " + ostatnia_litera_imienia)
input("Wiesz co?")
print("jutro będzie cudowny dzień!")
