def conversor(pais, valor):
    pesos = int(
        input(
            f"""{
                nombre.capitalize()
            } introduce la cantidad de pesos {
                pais.capitalize()
            }: $"""
        )
    )
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

nombre = input(
    '\nHola, cual es tu nombre? '
)

menu = int(
    input(
        f"""
Bienvenido {nombre} al conversor de pesos a dolares

1.-Pesos Mexicanos
2.-Pesos Argentinos
3.-Pesos Colombianos
        
Elige una opcion: """
    )
)

if menu == 1:
    conversor('Mexicanos', 19.83)
elif menu == 2: 
    conversor('Argentinos', 545.64)
elif menu == 3:
    conversor('Colombianos', 4895.54)
else:
    txt = 1
    while txt <= 200:
        print(
            f"""{
                txt
            }: {
                nombre.capitalize()
            } elige una opcion correcta"""
        )
        txt += 1