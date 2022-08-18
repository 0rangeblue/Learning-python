import random

def run():
    numero_aleatorio = random.randint(1, 4000)
    numero_elegido = int(input("Elige un numero del 1 al 4000: "))
    while numero_elegido != numero_aleatorio:
        if numero_elegido < numero_aleatorio:
            print("\nBusca un numero mas grande")
        else:
            print("\nBusca un numero mas chico")
        numero_elegido = int(input("Elige otro numero: "))
    print("\nGANASTE")

if __name__ == "__main__":
    run()