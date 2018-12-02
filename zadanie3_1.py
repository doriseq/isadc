lista = [0,0,0]
lista[0] = input('Podaj pierwszą nazwę: ')
lista[1] = input('Podaj drugą nazwę: ')
lista[2] = input('Podaj trzecią nazwę: ')

print(('+' + ('-' * 15))*3 + '+')
for i in range(3):
    if len(lista[i]) > 15:
        lista[i] = ((lista[i])[0:12] + "...")
    print(("|" + lista[i].center(15)), end='')
    if i == 2:
        print("|")
print(('+' + ('-' * 15))*3 + '+')
