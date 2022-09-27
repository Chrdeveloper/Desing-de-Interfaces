from fibonacci import funcion_fibonacci
n = -1
while(n <= 0):
	n = int (input("Introduce numero positivo"))
print("Secuencia de fibonacci de "+str(n))
print(funcion_fibonacci(n))
