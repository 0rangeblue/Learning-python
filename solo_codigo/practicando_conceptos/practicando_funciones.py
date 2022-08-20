def conversor(pais, valor):
    pesos = int(input(f"""\n{
        nombre.capitalize()
        } introduce la cantidad de pesos {
            pais.capitalize()} a convertir: """))
    dolares = pesos / valor 
    print(f"""\n{nombre.capitalize()} tienes ${str(
                round(dolares, 2))} dolares""")

nombre = input(
    '\nHola, cual es tu nombre? '
)

menu = int(
    input(
        f"""\nBienvenido {
            nombre.capitalize()
        } al conversor de pesos a dolares:
        
        1.-Pesos Mexicanos
        2._Pesos Colombianos
        3.-Pesos Argentinos
        4.-Pesos Peruanos
        5.-Pesos Venezolanos
        6.-Pesos Chilenos
        7.-Pesos Uruguayos
        8.-Pesos Bolivianos
        9.-Pesos Guatemaltecos
        
        Elige una opcion: """
    )
)

if menu == 1:
    conversor('mexicanos', 19.84)
elif menu == 2:
    conversor('colombianos', 4167.34)
elif menu == 3:
    conversor('argentinos', 134.54)
elif menu == 4:
    conversor('peruanos', 3.87)
elif menu == 5:
    conversor('venezolanos', 248303.10)
elif menu == 6:
    conversor('chilenos', 875.76)
elif menu == 7:
    conversor('uruguayos', 40.10)
elif menu == 8:
    conversor('bolivianos', 6.90)
elif menu == 9:
    conversor('guatemaltecos', 7.74)
else:
    txt = 1
    while txt <= 48:
        print(
            f"""{
                txt}: {
                nombre.capitalize()
            } elige una opcion correcta."""
        )
        txt += 1