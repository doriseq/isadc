# print("Wzór na pole powierzchni koła ma postać: P = Pi*r^2")
# print("P - pole powierzchni koła")
# print("r - promień koła")
# pi = 3.14
# r = input("Podaj promień koła: ")
# promien = float(r)
# print("r^2= ")
# r_2 = promien**2
# print(r_2)
# print("P= ")
# print(pi*r_2)

def pole_kola(r):

    promien = float(r)
    r_2 = promien ** 2
    return (3.14 * r_2)


r = input("Podaj promień koła: ")
print(pole_kola(r))


