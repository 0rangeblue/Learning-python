import random 

def generar_contrasenas():
    MAYUS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z']
    MINUS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z']
    NUMS = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    CHARS = ['@', '?', '!', '[', '{', '(', ')', '}', ']', '>', '<', '$', '#', '%']

    caracteres = MAYUS + MINUS + NUMS + CHARS

    contrasena = []

    for i in range(32):
        caracter_random = random.choice(caracteres)
        contrasena.append(caracter_random)

    contrasena = "".join(contrasena)
    return contrasena

def run():
    contrasena = generar_contrasenas() 
    print("Your new password is: " + contrasena)


if __name__  == "__main__":
    run()