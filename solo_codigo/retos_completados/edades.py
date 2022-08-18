nombre1 = input('Hola, cual es tu nombre? ')
nombre2 = input(f'Bienvenido {nombre1.capitalize()}, como se llama tu amigo? ')

edad1 = int(input(f'Hola {nombre1.capitalize()}, introduce tu edad: '))
edad2 = int(input(
    f'Hola de nuevo {nombre1.capitalize()}, introduce la edad de tu amigo {nombre2.capitalize()}: '))

if edad1 < edad2:
    print(f'\n{nombre1.capitalize()}, eres menor que {nombre2.capitalize()}!')
elif edad1 > edad2:
    print(f'\n{nombre1.capitalize()}, eres mayor que {nombre2.capitalize()}')
else:
    print(f'\n{nombre1.capitalize()} y {nombre2.capitalize()} tienen la misma edad.')