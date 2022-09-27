from fibonacci import funcion_fibonacci
from fibonacci2 import funcion_fibonacci2
import time
n = -1
while(n <= 0):
	n = int (input("Introduce numero positivo"))

opcion = input("Mediante que opcion quieres hacer la operacion(a/b)")
if(opcion == "a"):
	print("Secuencia de fibonacci de "+str(n))
	start_time = time.time()
	print(funcion_fibonacci(n))
	end_time = time.time()
	elapsed_time = end_time - start_time
	print("Tiempo de ejecucion: "+str(elapsed_time)+" s")
else:
	print("Secuencia de fibonacci de "+str(n))
	start_time = time.time()
	print(int (funcion_fibonacci2(n)))
	end_time = time.time()
	elapsed_time = end_time - start_time
	print("Tiempo de ejecucion: "+str(elapsed_time)+ " s")
