# 1 dolar a pesos en Mexico = 20.28
# 1 dolar a pesos en Argentina = 125.45
# 1 dolar a pesos en Colombia = 4205.04

def conversor(pais, valor_dolar):
    pesos = int(input("\nCuantos pesos " + pais + " tienes? "))
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    print("Tienes $" + str(dolares) + " dolares")

menu = """ 
         BIENVENIDO AL CONVERSOR DE PESOS A DOLARES
                    
                    1 - Pesos Mexicanos
                    2 - Pesos Argentinos
                    3 - Pesos Colombianos

ELIGE UNA OPCION: """

MXN = 20.28
ARG = 125.45
COL = 4205.04

opcion = int(input(menu))

if opcion == 1:
    conversor("mexicanos", MXN)
elif opcion == 2:
    conversor("argentinos", ARG)
elif opcion == 3:
    conversor("colombianos", COL)
else:
    print("Elige una opcion correcta")