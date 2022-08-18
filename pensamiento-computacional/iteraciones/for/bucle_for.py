# Nota agregar una opcion que deje ver diferentes tablas en infinito, codigo:
# elif numero < 0:
#     while numero < 0:
#         numero_nuevo = int(
#             input(
#                 f'\nALERTA INGRESASTE UN NUMERO NEGATIVO, VUELVE A INTENTARLO: {menu}'
#                 )
#         )
#         print('\n')    
#         for i in range(1, 11):
#             print(f'{numero_nuevo} x {i} es = {numero_nuevo * i}')
# has entrado al modo de tablas infinitas, escribe exit para salir

def negative_repetition():
    numero_nuevo = int(input(reset_menu))
    if  numero_nuevo < 0:
        while numero_nuevo < 0:
            numero_nuevo = int(input(reset_menu))
            if numero_nuevo > 0:    
                print(f'\nTABLA DEL {numero_nuevo}:')
                for i in range(1, 11):
                    print(f'{numero_nuevo} x {i} es = {numero_nuevo * i}')
    else:
        print(f'\nTABLA DEL {numero_nuevo}:')
        for i in range(1, 11):
            print(f'{numero_nuevo} x {i} es = {numero_nuevo * i}')

def infinite_negative_repetition():
    numero_nuevo = int(input(reset_menu))
    if numero_nuevo < 0:
        while numero_nuevo < 0:
            infinite_negative_repetition()
    else:
        print(f'\nTABLA DEL {numero_nuevo}')
        for i in range(1, 11):
            print(f'{numero_nuevo} x {i} es = {numero_nuevo * i}')
        infinite_pattern()

def negative_infinite():
    new_num = int(input(reset_menu))
    if new_num < 0:
        while new_num < 0:
            negative_infinite()
    else:
        print(f'\nTABLA DEL {new_num}')
        for i in range(1, 11):
            print(f'{new_num} x {i} es = {new_num * i}')
        infinite_pattern()

def pattern():
    numero_inf = int(input(f'\nBienvenido al modo de tablas infinitas, ingresa un numero positivo de la tabla que quieras ver: '))
    if numero_inf > 0:
        print(f'\nTABLA DEL {numero_inf}:')
        for i in range(1, 11):
            print(f'{numero_inf} x {i} es = {numero_inf * i}')
        infinite_pattern()
    else:
        infinite_negative_repetition()

def infinite_pattern():
    infinite_number = int(input('\nIngresa un numero positivo de la tabla que quieras ver: '))
    if infinite_number > 0:
        while infinite_number > 0:
            print(f'\nTABLA DEL {infinite_number}:')
            for i in range(1, 11):
                print(f'{infinite_number} x {i} es = {infinite_number * i}')
            infinite_pattern()
    else:
        negative_infinite()
        

menu = f"""
Bienvenido al menu de tablas de multiplicar.
Este script tiene todas las tablas de multiplicar existentes del 1 al 10 dentro de la tabla.

1.-Modo de tabla unica
2.-Modo de tablas infinitas

Elige una opcion: """

reset_menu = f"""\nALERTA, INGRESASTE UN NUMERO NEGATIVO, VUELVE A INTENTARLO:
Ingresa un numero positivo de la tabla que quieras ver: """

opciones = int(input(menu))

if opciones == 1:
    uniq_table = int(input(f"""\nBienvenido al modo de tabla unica, ingresa un numero positivo de la tabla que quieras ver: """))
    if uniq_table > 0:
        print(f'\nTABLA DEL {uniq_table}:')
        for i in range(1, 11):
            print(f'{uniq_table} x {i} es = {uniq_table * i}')
    else:
        negative_repetition()
elif opciones == 2:
    pattern()
else:
    txt = 1
    print('\n')
    while txt <= 25:
        print(f'{txt}: Vuelve a intentarlo y elige una opcion correcta.')
        txt += 1