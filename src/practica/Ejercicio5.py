################
# Nombre - @BenitezMagali
# UNRN Andina - Introducción a la Ingenieria en Computación
################
"""
5. Corchetes balanceados
Implementar una función que determine si una cadena con corchetes está balanceada.

Es decir, si cada corchete que abre, tiene su par que cierra. El resultado debe ser un valor lógico indicando si esta o no balanceado.

Ejemplos

   (vacio)      True
   []           True
   [][]         True
   [[][]]       True
   ][           False
   ][][         False
   []][[]       False
La funcion deberia de ignorar todo lo que no sean corchetes.

Extra #1
Hacer que la funcion reciba que par de simbolos buscar si esta balanceado. (como para pasar parentesis, llaves o cualquier otro)

Extra #2
Hacer que la función verifique el balanceo simultaneo de parentesis, llaves y corchetes."""

def corchetes_balanceados(cadena_con_corchetes):
	balanceado=True
	i=0
	j=len(cadena_con_corchetes)
	while i<len(cadena_con_corchetes) and balanceado==True:
		if cadena_con_corchetes[i]=="[":
			corcheteCierreEncontrado=False
			while j>i and corcheteCierreEncontrado==False:
				if(cadena_con_corchetes[j-1]=="]"):
					corcheteCierreEncontrado=True
				j-=1
			if corcheteCierreEncontrado==False:
				balanceado=False
			
		i +=1
				
	return balanceado


print(corchetes_balanceados(""))
print(corchetes_balanceados("[]"))
print(corchetes_balanceados("[][]"))
print(corchetes_balanceados("[[][]]"))
print(corchetes_balanceados("]["))
print(corchetes_balanceados("][]["))
print(corchetes_balanceados("[]][[]"))