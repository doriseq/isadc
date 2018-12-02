zmienna = 13.330

print("wartość to: %s" % zmienna)
print("wartość to: %f" % zmienna)
print("wartość to: %d" % zmienna)

print("to jest {} sposób na wprowadzenie {}".format(3, 'zmiennych'))
print("to jest {ilosc} sposób na wprowadzenie {nazwa}".format(ilosc=3, nazwa = 'zmiennych'))
print("to jest {ilosc} sposób na wprowadzenie {nazwa}".format(nazwa = 'zmiennych', ilosc=3)) # tylko dla danej linii sie wyświetla print(ilość) w oddzielnej linii nie zadziała

zdanie = 'encyklopedia'
print(zdanie[::-1])


print(range(3))
print(type(3))

lista = [1,2,3]
print(lista)
lista_2 = ["kwiatek","doniczka"]
print(lista_2)
lista_3 = []
print(lista_3)

lista4 = list('ewa')
print(lista4)

range1 = range(1,25)
lista5 = list(range1)
del(lista5[5])
print(lista5)

lista6 = [
    [1,2,3],
    [4,5,6,'NAPIS'],
    [7,8,9]
]
print(lista6[1][3][2])

x=0
while(x<10):
    print('wyświetl mnie!')
    x += 1


decyzja = None
while(decyzja != 'T'):
    decyzja = input("Wciśnij 'T' aby zakończyć program")

