print('Podaj rok, a powiem Ci czy jest przestępny')
rok = input("Wpisz rok")
data = float(rok)
warunek_1 = data % 4
warunek_2 = data % 100
warunek_3 = data % 400
if (warunek_1 == 0 and warunek_2 != 0 or warunek_3 == 0):
    print('tak')
else:
    print('nie')