numero = 1
numero 
1
numero = 4
numero 
4
numeros = [1, 3, 6, 8, 9, 45, 90]
numeros
[1, 3, 6, 8, 9, 45, 90]
objetos = ["Hola", 3, 4.5, True]
objetos
["Hola", 3, 4.5, True]
objetos[1]
3
objetos[0]
"Hola"
objetos[3]
True
objetos[4]
IndexError: list index out of range
objetos 
["Hola", 3, 4.5, True]
objetos.append(False)
objetos 
["Hola", 3, 4.5, True, False]
objetos.append(1)
objetos
["Hola", 3, 4.5, True, False, 1]
objetos.pop(1)
3
objetos 
["Hola", 4.5, True, False, 1]
for elemento in objetos:
    print(elemento)
"Hola"
4.5
True
False 
1
objetos[::-1]
[1, False, True, 4.5, "Hola"]
objetos[1:3]
[4.5, True]