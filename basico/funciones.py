menu = """
    BIENVENIDO AL CONVERSOR DE PESOS A DOLARES

1 - Pesos Mexicanos
2 - Pesos Argentinos
3 - Pesos Colombianos

ELIGE UNA OPCION: """

opcion = int(input(menu))

def conversor(pais, valor):
    pesos = int(input("Cuantos pesos " + pais + " tienes? "))
    dolares = pesos / valor
    dolares = round(dolares, 2)
    print("Tienes $" + str(dolares) + " dolares")

if opcion == 1:
    conversor("mexicanos ", 19.88)
elif opcion == 2:
    conversor("argentinos ", 60)
elif opcion == 3:
    conversor("colombianos ", 3284)
else:
    print("Elige una opcion correcta")