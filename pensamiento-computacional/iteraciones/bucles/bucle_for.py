comprobar = True

while comprobar == True:
    numero = int(input('Bienvenido al programa de tablas de multiplicar, ingresa un numero positivo: '))
    if numero > 0:
        comprobar = False
        print(f'\nTABLA DEL {numero}')
        for i in range(1, 11):
            print(f'{numero} x {i} es = {numero * i}')
            i += 1
    else:
        print('ALERTA: ingresaste un numero negativo, vuelve a intentarlo con un numero positivo.')

