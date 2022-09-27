import random

def pregunta1():
	print("Cuantos titulos mundiales tiene Ayrton Senna?")
	print("a.- 4")
	print("b.- 7")
	print("c.- 3")
	respuesta = input("Elige opcion (a/b/c)")
	if(respuesta == "c"):
		puntuacion = 10
	else:
		puntuacion = -5
	return puntuacion
	
def pregunta2():
	print("Donde gano Mechael Schumaquer su ultima carrera?")
	print("a.- Brasil")
	print("b.- China")
	print("c.- Argentina")
	respuesta = input("Elige opcion (a/b/c)")
	if(respuesta == "b"):
		puntuacion = 10
	else:
		puntuacion = -5
	return puntuacion

def pregunta3():
	print("Cual es el unico piloto en haber ganado un mundial sin hacer poles")
	print("a.- Ayrton Senna")
	print("b.- Niki Lauda")
	print("c.- Juan Pablo Montoya")
	respuesta = input("Elige opcion (a/b/c)")
	if(respuesta == "b"):
		puntuacion = 10
	else:
		puntuacion = -5
	return puntuacion
	
print("Seleccion aleatoria de preguntas")
intentos = 0
resultado = 0
while(intentos <= 1):
	n = random.randint(1,3)
	if(n == 1):
		resultado += pregunta1()
	if(n == 2):
		resultado += pregunta2()
	if(n == 3):
		resultado += pregunta3()
	intentos += 1
	
print("Resultado es...."+str(resultado))
