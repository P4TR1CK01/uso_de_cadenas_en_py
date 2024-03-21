'''
import sys   # libreria para leer argumentos del programa
import time # libreria para esperar un segundo
i= int(sys.argv[1])
print(i)
while i > 0:
  print('Tiempo restante: ', i)
  time.sleep(1)
  i -= 1
  
print('booom')'''

def sigma():
  #sumamos la suma de los numeros del 1 al 100
  suma = 0
  argumentos = sys.argv
  limite = int(argumentos[1])
  #iniciamos un iterador
  i = 1
  # condicion para seguir iterando
  while i <= limite:
    suma = suma + i
    #incrementamos el iterador
    i = i + 1
  print(suma)

def sigmaFor():
  suma = 0
  for i in range(1,101,1):
    suma += i
  print(suma)

sigmaFor()
#main()
#sigma()







'''def main():
  argumentos = sys.argv 
  segundos = argumentos[1]
  time.sleep(1)
  print(segundos)


main()'''

# sys.argv en Python es una lista de argumentos de línea de comandos pasados a un script de Python. Aquí está su función:
'''
sys.argv[0] es el nombre del script. Dependiendo del sistema operativo, puede ser una ruta completa o simplemente el nombre del archivo.
Si ejecutas el comando usando la opción -c en la línea de comandos del intérprete, sys.argv[0] se establece en la cadena de caracteres -c.
En resumen, sys.argv te permite acceder a los argumentos pasados al script cuando lo ejecutas desde la línea de comandos. Por ejemplo, si ejecutas python mi_script.py argumento1 argumento2, sys.argv contendrá ['mi_script.py', 'argumento1', 'argumento2'].          
# obtener la cantidad de segundos desde los argumentos
'''



# un argumento es todo lo que escribo cuando se ejecuta el programa
'''
python bomba de tiempo 5
5
4
3
2
1
booom¡¡¡¡¡
'''