'''
voy a iterar preguntando el nombre de la especie
voy a realizar un ciclo infinito
En cada ocacion pregunto lo sgte:
- nombre de la especie
-Precio de la unidad
-cantidad de ejemplares

Si el usuario ingresa como nombre de la especie un '0', entonces
termina el ciclo. Imprimo la lista de todas las mascotas
Bonus: Una vez finalizado el ciclo imprimir el total de dinero en especies
usar bucle while
'''

'''mascotas = [
  {
    'especie': 'Perro',
    'precio': 10000
    'cantidad': 8
  }
]'''
'''
mascotas = []

def tienda():
  while  True:
    especie = input('Ingrese el nombre de la especie (o "0" para terminar): ')
    if especie == '0':
      break
    
    precio = float(input('ingrese el precio de la unidad: '))
    cantidad = int(input('ingrese la cantidad de ejemplares: '))
    
    mascota = {
      'especie' : especie,
      'precio' : precio,
      'cantidad' : cantidad
    }
  
    mascotas.append(mascota)
    
    print('\nLista de tdoas las mascotas: ')
    for mascota in mascotas:
      print(f'Especie: {mascota['especie']}, Precio: ${mascota['precio']}, cantidad: {mascota['cantidad']}')
        
    total_costo = sum(mascota['precio'] * mascota['cantidad'] for mascota in mascotas)
    print(f'\nTotal de dinero en especies: ${total_costo}')
    
tienda()'''

'''
# diccionario ejemplo update
auto ={
  'marca' : 'Mazda',
  'modelo': '323',
  'motor' :  2000
}

auto.update({
  'color' : 'negro',
  '4x4'   : False
})
print(auto)    '''


print('Bienvenidos al ADMIN de la tienda de mascotas')
def tienda ():
  mascotas = []
  
  while True:
    #1. Pedimos los 3 datos de cada tipo de mascota
    especie = input('Ingrese la nueva especie:\n ')
    #revisamos de inmediato si el usuario no desea agregar más mascotas
    if especie == "0":
      break
    precio = int(input('Ingrese el precio por ejemplar:\n '))
    cantidad = input('Ingrese el numero de ejemplares:\n ')
    
    cantidad = int(cantidad)
    #2. Armamos nuestro diccionario
    nueva_mascota = {
      'especie' : especie,
      'precio'  : precio,
      'cantidad': cantidad 
    }
    #3. Agregamos el diccionario a la lista de mascotas
    mascotas.append(nueva_mascota)
  print(mascotas)
  
  #5. Calculamos el total de $ en el inventario
  total = 0
  for mascota in  mascotas:
    total += mascota['precio'] * mascota['cantidad']
    
  print(f'En total en la tienda hay ${total} en especies')
tienda()
    