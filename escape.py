####Actividad 1 - Velocidad de escape

'''
1. Se solicita crear un script escape.py que permita calcular la velocidad de escape
ingresando como datos de entradas el radio r y la constante g. Los datos de entrada
deben ingresarse de manera interactiva utilizando la función input().
(2,5 Puntos)

2. El programa debe especificar claramente el formato en el que se deben entregar los
datos de entrada con instrucciones apropiadas.
(2,5 Puntos)

Ejemplo:
“Ingrese el radio en Kilómetros:”,
“Ingrese la constante g: ”
La respuesta del programa también debe mostrarse con un texto apropiado:
Ejemplo:
“La velocidad de Escape es 11174.6 [m/s]”
Para verificar el correcto funcionamiento del programa, se puede verificar con
los siguientes datos:
○g = 9.8 [m/s2]
r = 6371 [Km]
Se obtiene como resultado:
Velocidad de Escape = 11174.6 [m/s]

'''
#empezamos con el programa escape.py

#importamos libreia math
import math


def calculo_vel_esc():                                          #definimos la funcion calculo_vel_esc

  radio = float(input('Ingrese el radio en Kilómetros: '))      #pedimos al usuario que ingrese el radio en km
  g = float(input('Ingrese la constante g: '))                  #pedimos al usuario que ingrese la constante g
  velocidad = math.sqrt(2 * g * radio * 1000)                   #calculamos la velocidad de escape
  print('La velocidad de Escape es' , velocidad, '[m/s]')       #imprimimos la velocidad de escape

calculo_vel_esc()                                               #llamamos a la funcion calculo_vel_esc      




'''import math: Esta línea importa el módulo math, que proporciona funciones matemáticas.'''
'''def calculo_vel_esc():: Esta línea define una función llamada calculo_vel_esc. Las funciones son bloques de código reutilizables que realizan una acción específica.'''
'''radio = float(input('Ingrese el radio en Kilómetros: ')): Esta línea pide al usuario que ingrese el radio en kilómetros y convierte la entrada del usuario a un número de punto flotante.'''
'''g = float(input('Ingrese la constante g: ')): Similar a la línea anterior, esta línea pide al usuario que ingrese la constante gravitacional y convierte la entrada del usuario a un número de punto flotante.'''
'''velocidad = math.sqrt(2 * g * radio * 1000): Esta línea calcula la velocidad de escape utilizando la fórmula de la velocidad de escape y los valores ingresados por el usuario.'''
'''La función math.sqrt calcula la raíz cuadrada de un número.'''
'''print('La velocidad de Escape es' , velocidad, '[m/s]'): Esta línea imprime la velocidad de escape calculada.'''
'''calculo_vel_esc(): Esta línea llama a la función calculo_vel_esc, lo que hace que se ejecute el código dentro de la función.'''
'''La función calculo_vel_esc solicita al usuario que ingrese el radio en kilómetros y la constante gravitacional, y luego calcula la velocidad de escape utilizando la fórmula de la velocidad de escape. Finalmente, imprime la velocidad de escape calculada en metros por segundo.'''
'''La función math.sqrt calcula la raíz cuadrada de un número.'''
'''La función print imprime un mensaje en la consola.'''
'''La función input solicita al usuario que ingrese un valor.'''
''''las funciones son bloques de código reutilizables que realizan una acción específica. En este caso, la función calculo_vel_esc realiza el cálculo de la velocidad de escape.'''
'''La función float convierte una cadena en un número de punto flotante. En este caso, se utiliza para convertir la entrada del usuario en un número decimal.'''