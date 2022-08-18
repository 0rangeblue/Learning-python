>>> '123'
'123'
>>> '123' * 3
'123123123'
>>> '123' + '456'
'123456'
>>> ('Hip ' * 3) + ' ' + 'hurra'
'Hip Hip Hip  hurra'

De una manera mucho mas legible se utiliza la cadena de formato que se identifican con esta f al principio en la cadena:
>>> f'{"Hip " * 3} hurra'
'Hip Hip Hip  hurra'

Podemos realizar diferentes tipos de operaciones en las cadenas pero tambien podemos aplicarles diferentes funciones como:
*len(longitud)
*indexing(indexacion)
*slicing(rebanadas)
	*my_str[comienzo:fin:pasos]
>>> my_var = 'platzi'
>>> len(my_var)
6

Para acceder a cada uno de estos caracteres podemos usar una notacion de indice pero antes hay que recordar que dentro de la ingenieria
de software y en general en las ciencias de computacion se comienza a contar desde el 0:
>>> my_var[0]
'p'
>>> my_var[1]
'l'
>>> my_var[2]
'a'

La notacion de rebanadas o Slicing es muy sencila pero al principio cuesta trabajo adaptarse a ella:
>>> my_var[comienzo:final:pasos]
>>> my_var[2:]
'atzi'
>>> my_var[:3]
'pla'

Cuando nosotros llegamos al final ahi si no lo cuenta, no es inclusivo por eso llego a 'pla'.

Tambien podemos restar valores del str:
>>> print(my_var)
platzi
>>> my_var[:-2]
'plat'
>>> my_var[:-1]
'platz'
>>> my_var[:-4]
'pl'

Y podemos decir que queremos toda la cadena desde el principio hasta el final y queremos ir saltando de 2 en 2 por ejemplo:

>>> print(my_var)
platzi
>>> my_var[::2]
'paz'
>>> my_var[::1]
'platzi'
>>> my_var[::3]
'pt'

Concatenacion con valor en el str:
>>> 'Yo estudio en ' + my_var.capitalize()
'Yo estudio en Platzi'

En cadena de formato:
>>> f'Yo estudio en {my_var.capitalize()}'
'Yo estudio en Platzi'

Para multiplicarlo muchas veces
>>> print(f'Yo estudio en {my_var.capitalize()}, ' * 5)
Yo estudio en Platzi, Yo estudio en Platzi, Yo estudio en Platzi, Yo estudio en Platzi, Yo estudio en Platzi,

Cadenas(strings)
*Los objetos de tipo str pueden representarse con "" o ''
*El operador + tiene diferente significado segun el tipo de dato. Con cadenas significa concatenacion
*El operador * es el operador de repeticion con cadenas
*Las cadenas son inmutables
Las cadenas son inmutables, esto significa que una vez que las declaramos en memoria ya no podemos cambiarlas, nosotros podemos
reasignar una variable a una cadena distinta pero la que declaramos al principio una vez que se declara ya no puede cambiarse

Con todo esto ya vimos como funcionan las cadenas y que tipos de operaciones podemos realizar en ellas, estas no son todas las
operaciones.

Entradas:
>>> nombre = input('Cual es tu nombre: ')
Cual es tu nombre: rs3c
>>> print(nombre)
rs3c
>>> print('Tu nombre es ' + nombre.capitalize())
Tu nombre es Rs3c
>>> nombre
'rs3c'
>>> print(f'Tu nombre es {nombre}')
Tu nombre es rs3c
>>> print(f'Tu nombre es {nombre.capitalize()}')
Tu nombre es Rs3c

Entradas con numero:
>>> numero = input('Escribe un numero: ')
Escribe un numero: 53
>>> numero
'53'
>>> print(type(numero))
<class 'str'>

Esta en valor de string no de numero, para convertirlo a numero:
>>> numero = int(numero)
>>> print(type(numero))
<class 'int'>
>>> numero
53

De otra forma inicial:

>>> num = int(input('Escribe un numero: '))
Escribe un numero: 44
>>> num
44
>>> print(type(num))
<class 'int'>

Con todo esto nosotros ya sabemos como trabajar con tipos escalares y con tipos no escalares es decir aquellos tipos que tienen una
estructura interna en el caso de la cadena son simplemente la secuencia de caracteres en la que esta compuesta esta cadena y tambien
sabemos como recibir inputs del usuario, esto ya nos da muchisima mas flexibilidad en cuanto a los tipos de programas que nosotros
podemos desarrollar.

Reto generar un programa que reciba el nombre del usuario y le de un saludo y que nos diga cual es la longitud de la cadena con todo
el saludo y el nombre:

>>> nombre = input('Hola, cual es tu nombre? ')
Hola, cual es tu nombre? rs3c
>>> saludo = (f'Hola {nombre}, la longitud de este texto es de {len(saludo)}')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'saludo' is not defined
>>> saludo = (f'Hola {nombre}, la longitud de este texto es de {len(nombre)}')
>>> saludo
'Hola rs3c, la longitud de este texto es de 4'
>>> print(saludo)
Hola rs3c, la longitud de este texto es de 4
>>> saludo = (f'Hola {nombre.capitalize}, la longitud de este texto es de {len(saludo)}')
>>> print(saludo
... )
Hola <built-in method capitalize of str object at 0x7f21987fe070>, la longitud de este texto es de 44
>>> print(saludo)
Hola <built-in method capitalize of str object at 0x7f21987fe070>, la longitud de este texto es de 44
>>> saludo = (f'Hola {nombre.capitalize()}, la longitud de este texto es de {len(saludo)}')
>>> print(saludo)
Hola Rs3c, la longitud de este texto es de 101
>>> saludo = (f'Hola {nombre.capitalize()}, la longitud de este texto es de {len(saludo)} caracteres')
>>> print(saludo)
Hola Rs3c, la longitud de este texto es de 46 caracteres


