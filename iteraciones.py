def visitar_ciiudades():
  ciudades = ['Puerto Mont', 'Talca', 'Valdivia', 'Santiago', 'Viña del Mar']
  for ciudad in ciudades:
    print(f'Este año visitaré: {ciudad}')

#visitar_ciiudades()


ciudades = ['Pto Mont', 'Talca', 'Valdivia', 'Santiago', 'Viña', 'Villa Alemana', 'Antofagasta']
#               0          1          2            3         4          5               6
print(ciudades[0])


def penultimo(lista):
  largo = len(lista)
  return lista[largo - 2]

#print(penultimo(['feña', 'vivi', 'max', 'Carlos', 'Esteban']))


for pos, ciudad in enumerate(ciudades):
  frase = f'La ciudad {ciudad} está en la posición {pos}'
# print(frase)



for indice, ciudad in enumerate(ciudades):
  frase = f'La ciudad {ciudad} está en la posición {indice}'
  if indice % 2 == 0:
    print(frase)