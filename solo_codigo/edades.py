from tkinter import N


nombre1 = input(
    '\nHola, como te llamas? '
)

nombre2 = input(
    f"""Bienvenido {
        nombre1.capitalize()
    }, ahora introduce el nombre de tu amigo: """
)

edad1 = int(
    input(
        f"""\n{
            nombre1.capitalize()
        } introduce tu edad: """
    )
)

edad2 = int(
    input(
        f"""Introduce la edad de tu amigo {
            nombre2.capitalize()
        }: """
    )
)

if edad1 < edad2:
    print(
        f"""\n{
            nombre1.capitalize()} eres menor que {
                nombre2.capitalize()
            }."""
    )

elif edad1 > edad2:
    print(
        f"""\n{
            nombre1.capitalize()} eres mayor que {
                nombre2.capitalize()
                }."""
    )

else:
    txt = 1
    while txt <= 50:
        print(
            f"""{
                txt}: {
                nombre1.capitalize()
            } y {
                nombre2.capitalize()
            } tienen la misma edad"""
        )
        txt += 1