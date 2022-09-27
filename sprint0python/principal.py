from fibonacci import funcion_fibonacci
from fibonacci2 import funcion_fibonacci2
n = -1
while(n <= 0):
	n = int (input("Introduce numero positivo"))

opcion = input("Mediante que opcion quieres hacer la operacion(a/b)")
if(opcion == "a"):
	print("Secuencia de fibonacci de "+str(n))
	print(funcion_fibonacci(n))
else:
	print("Secuencia de fibonacci de "+str(n))
	print(int (funcion_fibonacci2(n)))
