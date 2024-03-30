Algoritmo promedio
	Definir prom Como Real
	Escribir 'ingrese primera nota: '
	Leer nota1
	si nota1 < 1 O nota1 > 7 Entonces
		Escribir 'Nota no valida'
	SiNo
		Escribir 'ingrese segunda nota: '
		leer nota2
		si nota2 < 1 o nota2 > 7 Entonces
			Escribir 'nota no valida'
		SiNo
			 Escribir 'ingrese la tercera nota'
			 Leer nota3
			 si nota3 < 1 o nota3 > 7 Entonces
				 Escribir 'nota no valida'
			 SiNo
				 prom =redon((nota1 + nota2 + nota3)/3)
				 Escribir 'el promedio es: ', prom
				 si prom >= 4 Entonces
					 Escribir 'Ha aprovado el cusro'
				 SiNo
					 Escribir 'HA reprobado el curso'
				 FinSi
			 FinSi
		 FinSi
	 FinSi
FinAlgoritmo
