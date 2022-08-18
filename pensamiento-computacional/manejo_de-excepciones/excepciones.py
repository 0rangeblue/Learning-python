def dividir_elemen_lista(lista, divisor):
    try:
        return[i / divisor for i in lista]
    except ZeroDivisionError as e:
        divisor = int(input('Ingresa un divisor diferente de 0: '))
        return dividir_elemen_lista(lista, divisor)

def run():
    lista = list(range(10))
    divisor = 0
    print(dividir_elemen_lista(lista, divisor))

if __name__ == '__main__':
    run()