Algoritmo arreglos
	Definir pos como Entero 
	Dimension vacaciones[10]
	vacaciones[0] = "Sao Paulo"
	vacaciones[1] = "Ibiza"
	vacaciones[2] = "Houston"
	vacaciones[3] = "Venecia"
	vacaciones[4] = "Berlin"
	vacaciones[5] = "BS AS"
	vacaciones[6] = "Panamarimbo"
	vacaciones[7] = "Praga"
	vacaciones[8] = "Oslo"
	vacaciones[9] = "Lima"
	
	Escribir "Elija (p) para ciudades pares o (i) para ciudades impares"
	Leer eleccion_usuario
	Si eleccion_usuario == "p" Entonces
		pos = 0
	SiNo
		pos = 1
	FinSi
	// Vamos a recorrer todo el arreglo
	Escribir "Ciudades que si visitaré:"
	Mientras pos < 10 Hacer
		Escribir vacaciones[pos]
		pos <- pos + 2
	Fin Mientras
	
	// crear arreglo de 10 ciudades y preguntar al usuario si quiere recorrer ciudades pares o impares
	// Elija "p" para recorrer ciudades pares, "i" para recorrer ciudades impares
	
	
	
FinAlgoritmo
