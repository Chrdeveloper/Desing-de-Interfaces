
print("Cuantos titulos mundiales tiene Ayrton Senna?")
print("a.- 4")
print("b.- 7")
print("c.- 3")
respuesta = input("Elige opcion (a/b/c)")
puntuacion = 0 
if(respuesta == "c"):
	puntuacion += 10
else:
	puntuacion -=5
print("Donde gano Mechael Schumaquer su ultima carrera?")
print("a.- Brasil")
print("b.- China")
print("c.- Argentina")
respuesta = input("Elige opcion (a/b/c)")
if(respuesta == "b"):
	puntuacion += 10
else:
	puntuacion -=5
	print("Cual es el unico piloto en haber ganado un mundial sin hacer poles")
print("a.- Ayrton Senna")
print("b.- Niki Lauda")
print("c.- Juan Pablo Montoya")
respuesta = input("Elige opcion (a/b/c)")
if(respuesta == "b"):
	puntuacion += 10
else:
	puntuacion -=5

print("Tu puntuacion final es: "+ str(puntuacion))	
