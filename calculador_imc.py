'''El IMC, conocido también como el Índice de masa corporal, es una medida que asocia el
peso de una persona con su talla (su altura). Este valor es utilizado normalmente como un
indicador nutricional y constituye un índice fácil y sencillo de calcular para determinar el
estado de obesidad y sobrepeso de una persona. El IMC se calcula de la siguiente manera:
          
IMC = w/h al cuadrado

< 18.5 = bajo peso
[18.5 a 25[ = adecuado
25 a 30 = sobrepeso
30 a 35 = obesidad grado I
35 a 40 = obesidad grado II
> 40    = obesidad grado III 

En busca de mejorar la salud nutricional de los pacientes, se le solicita a usted como
programador el hecho de diseñar una herramienta que permita determinar el estado
nutricional de una persona
'''
#int = enteros / float = decimales 180 cm /100 = 1.80

'''
peso=float(input('ingrese su peso en kilogramos: '))
estatura=float(input('ingrese su estatura en metros: '))

imc = peso / estatura ** 2
if imc < 18.5:
  clasificacion = 'Bajo peso'
elif 18.5 <= imc < 25:
  clasificacion = 'Adecuado'
elif 25 <= imc < 30:
  clasificacion = 'sobrepeso'
elif 30 <= imc < 35:
  clasificacion = 'Obesidad grado I'
elif 35 <= imc < 40:
  clasificacion = 'Obesidad grado II'
else:
  clasificacion = 'Obesidad grado III'
print('su indice de masa corporal es de: '+str(imc))
print('Clasificacion de la OMS: ', clasificacion)
'''

peso=float(input('ingrese su peso en kilogramos: '))
estatura_cm=float(input('ingrese su estatura en centimetros: '))

estatura_m = estatura_cm / 100
imc = peso / estatura_m ** 2

if imc < 18.5:
  clasificacion = 'Bajo peso'
elif 18.5 <= imc < 25:
  clasificacion = 'Adecuado'
elif 25 <= imc < 30:
  clasificacion = 'sobrepeso'
elif 30 <= imc < 35:
  clasificacion = 'Obesidad grado I'
elif 35 <= imc < 40:
  clasificacion = 'Obesidad grado II'
else:
  clasificacion = 'Obesidad grado III'
print('su indice de masa corporal es de: '+ str(round(imc, 2)))
print('Clasificacion de la OMS: ', clasificacion)