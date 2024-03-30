##                      Fuerza bruta
'''
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
¿Qué tan seguro es tu password? ¿Intentemos hackear un password? Mediante el siguiente desafío se busca utilizar un algoritmo muy sencillo, 
llamado fuerza bruta para determinar cuántos intentos son necesarios para encontrar combinaciones numéricas en minúscula.
Para ello se ingresará un *password oculto. Este password puede contener sólo combinaciones de letras y se requiere determinar su seguridad.
Un mayor número de intentos implica un password más seguro:
El programa fuerza_bruta.py debe intentar todas las combinaciones de letras posibles, en orden alfabético, hasta que la combinación de letras sea igual a 
la de la contraseña indicada. Deberá hacer este proceso letra por letra, de izquierda a derecha.
Consideraciones ● Utilizar from string import ascii_lowercase ○ ascii_lowercase es un string con todas las letras del abecedario en minúsculas (sin la ñ).
● No considerar la ñ.
● Considera mayúsculas y minúsculas como una misma letra.
● Se considera "intento" cada vez que se compara una letra.

Ejemplo:
○ Usuario ingresa "abc"
○ El computador compara:
■ a es igual a a => Sí (1 intento), continúa con la siguiente letra.
■ b es igual a a => No (2 intentos), prueba otra comparación.
■ b es igual a b => Sí (3 intentos), continúa con la siguiente letra.
■ c es igual a a => No (4 intentos), prueba con otra comparación.
■ c es igual a b => No (5 intentos), prueba con otra comparación.
■ c es igual a c => Sí (6 intentos), continúa con la siguiente letra.
■ No hay más letras. Se adivinó la palabra en 6 intentos.
considere importar getpass
NOTA: A modo explicativo se mostrará la contraseña a buscar pero la idea es que ésta se ingrese de manera oculta. python fuerza_bruta.py Ingrese la contraseña: gato
La contraseña fue forzada en 43 intentos
#letras = 'abcdefghijklmnopqrstuvwxyz'
#passw = 'hola'
#intentos = 36
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''
'''
import getpass
from string import ascii_lowercase

contraseña = getpass.getpass("Ingrese su contraseña: ").lower()
caracteres  = ascii_lowercase
intentos = 0
  
for posicion in range(0, len(contraseña)):
    for intento in caracteres:
      intentos += 1
      if intento == contraseña[posicion]:
        break
  
print(f'contraseña: {contraseña}')
print(f'intentos: {intentos}')      
  
'''

import sys
from string import ascii_lowercase

def fuerza_bruta():
  clave = sys.argv[1].lower()
  intentos = 0
  for letra in clave:
    for caracter in ascii_lowercase:
      intentos += 1
      if letra == caracter:
        break
  print(f'Se logró romper la contraseña en {intentos} intentos')


  print(clave)
#fuerza_bruta()


