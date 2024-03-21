Funcion FizzBuzz (inicio , final)
	Definir i Como Entero 
	i = 1
	Mientras i <= 50 Hacer
		// imprimimos dependiendo el número
		si ( i mod 3 == 0) y (i mod 5 == 0) 
			Escribir "FizzBuzz"
		SiNo
		si i mod 3 == 0 Entonces
			Escribir ("Fizz")
		SiNo
			si i mod 5 == 0 Entonces
				Escribir ("Buzz")
			SiNo
				Escribir (i)
			FinSi
		FinSi
	FinSi
		//El incremento
		i = i + 1
	FinMientras
FinFuncion

Algoritmo sin_titulo
	FizzBuzz(3 , 5)
FinAlgoritmo
