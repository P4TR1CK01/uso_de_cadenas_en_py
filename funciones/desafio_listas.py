import sys

def word_count():
  #1. obtenemos el nombre del archivo
  nombre_archivo = sys.argv[1]
  #2. leemos el contenido del archivo
  with open(nombre_archivo, 'r') as file:
    texto = file.read()
  #3. contamos las letras
  texto_sin_espacios = [letra for letra in texto if letra != ' ']
  print(f'En el archivo hay (sin contar los espacios) {len(texto_sin_espacios)} letras')
  #4.  contamos las palabras
  num_palabras = len(texto.split(' '))
  print(f'Hay {num_palabras} palabras')
  
word_count()