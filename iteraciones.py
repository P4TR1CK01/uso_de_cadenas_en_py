'''def visitar_ciiudades():
  ciudades = ['Puerto Mont', 'Talca', 'Valdivia', 'Santiago', 'Viña del Mar']
  for ciudad in ciudades:
    #print(f'Este año visitaré: {ciudad}')

#visitar_ciiudades()

#def penultimo(lista):
  largo = len(lista)
  return lista[largo - 2]

#print(penultimo(['feña', 'vivi', 'max', 'Carlos', 'Esteban']))


for pos, ciudad in enumerate(ciudades):
  frase = f'La ciudad {ciudad} está en la posición {pos}'
# print(frase)

'''

'''
def visitar_ciudades():
ciudades = ['Pto Mont', 'Talca', 'Valdivia', 'Santiago', 'Viña', 'Villa Alemana', 'Antofagasta']
#               0          1          2            3         4          5               6
print(ciudades[0])

  for indice, ciudad in enumerate(ciudades):
    frase = f'La ciudad {ciudad} está en la posición {indice}'
    if indice % 2 == 0:
      print(frase)

def buscar(palabra):
  palabra = sys.argv[1]
  ciudades = ['Pto. Montt', 'Talca', 'Stgo', 'Valdivia', 'Viña', 'Villa Alemana', 'Antofagasta']
  # ahora buscamos la palabra
buscar(palabra)
'''
''
import sys   # libreria para leer argumentos del programa
def buscar():
  palabra = sys.argv[1]
  cuento = ['En', 'un', 'lugar', 'de', 'la', 'Mancha', 'de', 'cuyo', 'nombre', 'no', 'quiero', 'acordarme', 'no', 'ha', 'mucho', 'tiempo', 'que', 'vivía', 'un', 'hidalgo', 'de', 'los', 'de', 'lanza', 'en', 'astillero', 'adarga', 'antigua', 'rocín', 'flaco', 'y', 'galgo', 'corredor.']
  
  la_encontramos = False
  
  for pos, item in enumerate(cuento):

    if palabra == item:
      frase = f'La palabra {item} está en la posición {pos}'
      print(frase)
      la_encontramos = True
      break

  if not la_encontramos:
    print(f'La palabra {palabra} no está en el Quijjote de la Mancha')
# f sirve  para formatear cadenas, es como un string format pero mas potente y flexible

buscar()

'''
def quina ():

'''
#comprehension List´s
  lista = []
  for i in range(31):
    if i % 5 == 0:
      lista.append('Quina')
    else:
      lista.append(i)
'''

  lista = ['Quina' if i 5 % == 0 else i in range(31)]
  print(lista)

def crear_enlaces():
  nombres = ['Home', 'Nosotros', 'Contacto']
  enlaces = ['<a href="#"> + nombre + </a>' for nombre in nombres]
  print(enlaces)

crear_enlaces()



destinos = [
  {
    'nombre': 'Argentina'
    'prefijo': 54,
    'ciudades' : ['BS AS', 'Cordoba', 'Mendoza', 'Rio Gallegos']
  },
  
  {
    'nombre' : 'Suecia',
    'prefijo': 46,
    'ciudades' :['Estocolmo', 'Gotemburgo', 'Malmö', 'Kiruna']
  }
]
print(destinos[1]['ciudades'][2])