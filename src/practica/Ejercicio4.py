################
# Nombre - @BenitezMagali
# UNRN Andina - Introducción a la Ingenieria en Computación
################
"""4. Fibonacci
La sucesión de Fibonacci es una sucesión infinita donde cada elemento es la suma de los dos anteriores. 
En la misma, los dos primeros términos son 1. (En algunos lugares se toma el primer término en 0 y el segundo en 1) 
Implementar una función que permita obtener el n-esimo termino de la sucesión de Fibonacci. 
Siendo este número un entero positivo mayor a 2. """


def fibonacci_segun_termino(termino):
	fibonacci=[1,1]
	i=2
	while i<termino:
		fibonacci.append(fibonacci[i-1]+fibonacci[i-2])
		i+=1
	print(fibonacci)

fibonacci_segun_termino(4)
fibonacci_segun_termino(100)
