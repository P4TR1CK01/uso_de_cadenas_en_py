##                  Filtrado compacto
--------------------------------------------------------------------------------------------------------------
'''funcion ventas'''
#Una empresa provee de los balances del año anterior en un diccionario como se muestra a continuación:
--------------------------------------------------------------------------------------------------------------
import sys

def mayor_a():                  # El siguiente código define una función llamada `mayor_a()` que toma un solo argumento:
  ventas = {
    "Enero":      15000,
    "Febrero":    22000,
    "Marzo":      12000,
    "Abril":      17000,
    "Mayo":       81000,
    "Junio":      13000,
    "Julio":      21000,
    "Agosto":     41200,
    "Septiembre": 25000,
    "Octubre":    21500,
    "Noviembre":  91000,
    "Diciembre":  21000,
  }
  cantidad=sys.argv[1]           # Cantidad de meses a mostrar 
  cantidad=int(cantidad)        
  filtradas={llave: valor for llave, valor in ventas.items()  if valor > cantidad}  
  print(filtradas)
mayor_a()




funcion fuerza  bruta

#letras = 'abcdefghijklmnopqrstuvwxyz'
#passw = 'hola'
#intentos = 36'''