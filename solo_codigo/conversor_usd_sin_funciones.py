nombre = input(
    '\nCual es tu nombre? '
)

menu = int(
    input(
        f"""\nBienvenido {
            nombre
        } al conversor de pesos a dolares
        
        1.-Pesos Mexicanos
        2.-Pesos Argentinos
        3.-Pesos Colombianos
        
        Elige una opcion: """
    )
)

if menu == 1:
    pesos = int(
        input(
            f"""\n{
                nombre.capitalize()
            } introduce la cantidad de pesos Mexicanos que quieres convertir: $"""
        )
    )
    valor = 19.88
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
elif menu == 2:
    pesos = int(
        input(
            f"""\n{
                nombre.capitalize()
            } introduce la cantidad de pesos Argentinos que quieres convertir: $"""
        )
    )
    valor = 465.65
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
        } introduce la cantidad de pesos Colombianos que quieres convertir: $"""
        )
    )
    valor = 4658.34
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
else:
    txt = 1
    while txt <= 37:
        print(
            f"""{
                txt
            }: {
                nombre.capitalize()
            } escoge una opcion correcta, vuelve a intentarlo."""
        )
        txt += 1