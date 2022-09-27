def funcion_fibonacci2(n):
	A = (1 + (5** 0.5))/2
	#Parte A de la funcion
	B = (1 - (5** 0.5))/2
	#Part B de la funcion
	if(n <= 1):
		return n
	else: 
		return ((A ** (n)) - (B ** (n)))//(5**(0.5))
