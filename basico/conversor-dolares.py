menu = """
BIENVENIDO AL CONVERSOR DE PESOS A
DOLARES

1.-PESOS MEXICANOS
2.-PESOS ARGENTINOS
3.-PESOS COLOMBIANOS

ELIGE UNA OPCION: """

opcion = int(input(menu))

if opcion == 1:
    pesos = int(input
    ('\nCuantos pesos mexicanos tienes? '))
    valor_dolar = 19.88
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    print(
        "Tienes " + str(dolares)
        + " dolares")
elif opcion == 2:
    pesos = int(input(
        '\nCuantos pesos argentinos tienes? '
    ))
    valor_dolar = 843
    dolares = pesos / valor_dolar
    print("Tienes "
    + str(round(dolares, 2)) +
    " dolares")
elif opcion == 3:
    pesos = int(input(
        '\nCuantos pesos colombianos tienes? '
    ))
    valor_dolar = 4583
    dolares = pesos / valor_dolar
    print("Tienes " +
    str(round(dolares, 2)) +
    ' dolares')
else:
    print(
        '\nElige una opcion correcta'
    )
