numeros = [1, 2, 3, 4, 5]
numeros
[1, 2, 3, 4, 5]
numeros2 = [6, 7, 8 ,9]
numeros2 
[6, 7, 8, 9]
lista_final = numeros + numeros2 
lista_final
[1, 2, 3, 4, 5, 6, 7, 8, 9]
numeros * 5
[1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
mi_tupla = (1, 2, 3, 4, 5)
mi_tupla
(1, 2, 3, 4, 5)
mi_tupla.append(5)
# da error porque es un objeto estatico
for numero in mi_tupla:
    print(numero)
1
2
3
4
5

# Las tuplas son la estructura de datos mas rapida disponible en python, son inmutables
# inmutable = objeto que no puede cambiar