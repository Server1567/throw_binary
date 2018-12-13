#!/usr/bin/python3

"""
Crea una secuencia de números binarios en la cual deben ir cambiando de forma aleatoria
en lo que pasa el tiempo, con su único objetivo, EL DISEÑO DE LA CONSOLA. 
"""
__author__ = "Junior Jimenez"
__copyright__ = "Copyright 2018"
__license__ = "MIT License"
__version__ = "1.0"
__maintainer__ = "Junior Jimenez"
__email__ = "chapijalaj@gmail.com"
__status__ = "Developer"

from random import randint
import sys, time

array = []
y = False
lista = []

def action():
	# Esta función crea la lista con sus binarios aleatorios
	i = 0
	global array
	while i < 100:
		for x in range(1,80):
			array.append(str(randint(0, 1)))

		y = "".join(array)
		lista.append(y)
		array = []

		i += 1

	def flashing():
		# Esta función postea los números de las posiciones de la lista de forma asíncrona
		for i in range(len(lista)):
			time.sleep(0.01)
			sys.stdout.write("\r%d" % int(lista[i]))
			sys.stdout.flush()
	flashing()

if __name__ == "__main__":
	x = 0
	while x != 7:
		main = action()
		print(main)
		x += 1
		if x == 7: print("COMPLETE ENCRYPTION")






