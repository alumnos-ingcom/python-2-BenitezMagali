################
# Nombre - @BenitezMagali
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""1. Pares e impares
Escribir una función que retorne True cuando un número entero es par y False cuando no lo sea, sin utilizar módulo. (%) """

def par_impar(numero):
	resto=numero-2
	while resto>1:
		resto= resto-2

	if resto==1 or numero==1:
		return False
	elif resto==0:
		return True		

print(par_impar(3))
print(par_impar(4))
print(par_impar(2))
print(par_impar(1))
print(par_impar(0))