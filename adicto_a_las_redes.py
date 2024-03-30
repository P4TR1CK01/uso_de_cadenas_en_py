def ejemplos():
  seconds = [100, 50, 1000, 5000, 1000, 500]
  minutos = [numsecs / 60 for numsecs in seconds]
  print(minutos)

  nombres = ['Chingao', 'Florimar', 'Onur', 'Hernesto Lisama', 'Lazlo', 'Isaura']
  saludos = ['Hola' + nombre for nombre in nombres]
  print(saludos)

  rating = [50, 30, 45, 25, 55, 20]
  resultados = ['Buen rating' if puntos >= 45 else 'Mal rating' for puntos in rating]
  print(resultados)
def mostrar_semana():
  #'semana' es una variabl de tipo diccionario
  semana = {
    'lunes': 2,
    'martes': 2,
    'miercoles': 4,
    'jueves': 4,
    'viernes': 2,
  }
  print (semana['miercoles'])
  for llave, valor in semana.items():
    if valor == 2:
      print (f'el dia {llave} fué un día CORTO')
    else:
      print (f'el dia {llave} fue un DIA LARGO')

mostrar_semana()
'''

def mostrar_personaje():
  nombre = input('ingrese  el nombre de un personaje: ')
  planeta =  input ('Ingrese el planeta de origen del  personaje: ')
  poder = input('Ingrese la habilidad del personaje: ')
  moral = input('Ingrese moral del personaje si es bueno o malo: ')

  personaje = { 
    'nombre': nombre,
    'planeta': planeta,
    'poder': poder,
    'esBueno': True if moral ==  'bueno' else False
  }
  for llave, valor in personaje.items():
    print(f'el valor de {llave} es: {valor}')

mostrar_personaje()
'''