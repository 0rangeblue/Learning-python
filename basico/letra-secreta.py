def run():
    iniciar = input(menu)
    intentos = 0
    if iniciar != "A":
        print("Escribe la opcion correcta")
    if iniciar == "A":
        while intentos < 5:
            letra = input("Cual es la letra secreta? ")
            letra = letra.lower()
            intentos += 1
            if letra == "r":
                print("Ganaste, la letra secreta es R")
                break
            if intentos == 5:
                print("Perdiste, intentalo de nuevo")


menu = """
Bienvenido al juego de adivinar letras:

Adivina la letra para ganar; solo tienes 5 intentos

Escribe A para comenzar: """


if __name__ == "__main__":
    run()