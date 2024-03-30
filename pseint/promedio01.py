def obtener_nota():                                         # Función que obtiene una nota válida
    while True:                                             # Ciclo que se repite hasta que se ingrese una nota válida
        nota = float(input('Ingrese la nota: '))            # float(input()) permite ingresar un número decimal /input() permite ingresar un valor
        if 1 <= nota <= 7:                                  # Condicional que verifica si la nota está en el rango de 1 a 7
            return nota                                     # Retorna la nota si es válida / return termina la función y devuelve un valor 
        else:                                               # Si la nota no es válida
            print('Nota no válida. Intente de nuevo.')      # Imprime un mensaje de error

def calcular_promedio(nota1, nota2, nota3):                 # Función que calcula el promedio de tres notas
    return round((nota1 + nota2 + nota3) / 3, 2)            # Retorna el promedio de las notas / round() redondea el resultado a dos decimales

nota1 = obtener_nota()                                      # Llama a la función obtener_nota() y guarda el valor en la variable nota1
nota2 = obtener_nota()                                      # Llama a la función obtener_nota() y guarda el valor en la variable nota2
nota3 = obtener_nota()                                      # Llama a la función obtener_nota() y guarda el valor en la variable nota3

promedio = calcular_promedio(nota1, nota2, nota3)           # Llama a la función calcular_promedio() y guarda el valor en la variable promedio / nota1, nota2 y nota3 son los argumentos de la función

print('El promedio es: ', promedio)                         # Imprime el promedio de las notas con un mensaje de texto

if promedio > 4:                                            # Condicional que verifica si el promedio es mayor a 4 / if permite ejecutar un bloque de código si se cumple la condición 
    print('Ha aprobado el curso')                           # Imprime un mensaje si la condición es verdadera    
else:                                                       # Si la condición es falsa / else permite ejecutar un bloque de código si no se cumple la condición / else siempre va después de un if
    print('Ha reprobado el curso')                        

# Nota: El código se encuentra en un archivo llamado promedio01.py
# Para ejecutarlo se debe abrir la terminal y escribir python3 promedio01.py
# Luego se debe presionar la tecla Enter
# Se debe seguir las instrucciones que aparecen en la terminal
# El programa solicita ingresar tres notas
# Luego imprime el promedio de las notas
# Y finalmente imprime si el estudiante aprobó o reprobó el curso
# Si el promedio es mayor a 4 imprime 'Ha aprobado el curso'
# Si el promedio es menor o igual a 4 imprime 'Ha reprobado el curso'
# El programa finaliza después de imprimir el mensaje de aprobación o reprobación
# El programa se puede ejecutar las veces que se desee
# El programa se puede modificar para calcular el promedio de más notas
# Se pueden agregar más funciones o condicionales
# Se pueden cambiar los mensajes que imprime el programa
# Se pueden cambiar los valores de las notas para probar diferentes casos de uso como notas con decimales o notas fuera del rango de 1 a 7
# Se pueden agregar más validaciones para verificar si las notas son válidas como letras o caracteres especiales
    