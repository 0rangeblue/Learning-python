nombre = input('\nHola, cual es tu nombre? ')

menu = int(input(f"""\n
Bienvenido {nombre.capitalize()} a este script de tablas de multiplicar: 

       1.-Tablas unicas
       2.-Tablas infinitas
            
Elige una opcion: """))

comprobar = True 

if menu == 1:
        while comprobar == True:
            numero = int(input('\nIngresa un numero positivo: '))
            if numero > 0:
                print(f'\nTABLA DEL {numero}')
                for i in range(1, 11):
                    print(f'{numero} x {i} es {numero*i}')
                comprobar = False
            else:
                print('Ingresaste un numero negativo, vuelve a intentarlo.')
elif menu == 2:
    while comprobar == True:
            numero = int(input(f"""\n
Para salir ingresa: 0
Ingresa un numero positivo: """))
            if numero > 0:
                print(f'\nTABLA DEL {numero}')
                i = 1
                while i < 11:
                    print(f'{numero} x {i} es {numero*i}')
                    i += 1
            elif numero == 0:
                comprobar = False
                print('\n0Gracias por usar este script, vuelva pronto :)')
            else:
                print('Ingresa un numero positivo')