nombre = input(
    'Hola, cual es tu nombre? '
)

menu = int(
    input(
        f"""\nBienvenido {
            nombre.capitalize()
        } al conversor de pesos a dolares:
        1.-Pesos Mexicanos
        2.-Pesos Argentinos
        3.-Pesos Colombianos
        4.-Pesos Peruanos
        Elige una opcion: """
    )
)

if menu == 1:
    pesos = int(
        input(
            f"""\n{
                nombre.capitalize()
            } introduce la cantidad de pesos Mexicanos a convertir: """
        )
    )
    valor = 19.83
    dolares = pesos / valor
    print = int(
        input(
            f"""\n{
                nombre.capitalize()
            } tienes ${
                str(
                    round(dolares, 2)
                )
            } dolares"""
        )
    )
elif menu == 2:
    pesos = int(
        input(
            f"""\n{
                nombre.capitalize()
            } introduce la cantidad de pesos Argentinos a convertir: """
        )
    )
    valor = 134.54
    dolares = pesos / valor 
    print(
        f"""\n{
            nombre.capitalize()
        } tienes ${
            str(
                round(dolares, 2)
            )
        } dolares"""
    )
elif menu == 3:
    pesos = int(
        input(
            f"""\n{
                nombre.capitalize()
            } introduce la cantidad de pesos Colombianos a convertir: """
        )
    )
    valor = 4167.34
    dolares = pesos / valor 
    print(
        f"""\n{
            nombre.capitalize()
        } tienes ${
            str(
                round(dolares, 2)
            )
        } dolares"""
    )