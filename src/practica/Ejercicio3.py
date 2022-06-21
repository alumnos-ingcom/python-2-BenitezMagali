################
# Nombre - @BenitezMagali
# UNRN Andina - Introducción a la Ingenieria en Computación
################
"""3. Súper-puestos
Desarrollar una función que indique el grado de superposición entre dos listas. Siendo 0 sin superposición y 
uno para cada elemento superpuesto.
['H', 'o', 'l', 'a', ' ', 'M', 'u', 'n', 'd', 'o']
y
['H', 'o', 'l', 'a']
Tienen una superposición de cuatro elementos.
Extra #1
Indicar en lugar de la cantidad de caracteres superpuestos, la posicion de inicio de la superposición. """

def superpuestos(lista1, lista2):
	cantSuperpuestos=0
	i=0

	while i<len(lista1) and i<len(lista2):
		if(lista1[i]==lista2[i]):
			cantSuperpuestos+=1
		i+=1


	return cantSuperpuestos

print(superpuestos(['H', 'o', 'l', 'a', ' ', 'M', 'u', 'n', 'd', 'o'],['H', 'o', 'l', 'a'])	)


def superpuestosExtra1IndicandoPosInicioSuperposicion(lista1, lista2):
	i=0
	posInicioSuperposicion=0
	primerSuperposicion=True
	while i<len(lista1) and i<len(lista2):
		if(lista1[i]==lista2[i]):
			if primerSuperposicion==True:
				posInicioSuperposicion=i

			primerSuperposicion=False
		i+=1
	return posInicioSuperposicion

print(superpuestosExtra1IndicandoPosInicioSuperposicion(['H', 'o', 'l', 'a', ' ', 'M', 'u', 'n', 'd', 'o'],['B', 'o', 'l', 'a'])	)
