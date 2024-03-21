import math

proteinas = float(input('Ingrese la cantidad de proteinas: \n'))
carbohidratos = float(input('Ingrese la cantidad de carbohidratos: \n'))
grasas = float(input('Ingrese la cantidad de grasas: \n'))
alcohol = float(input('Ingrese la cantidad de alcohol: \n'))

# calorias = 4 * (proteina + carbohidratos) + 9 * grasa
calorias = 4 * (proteina + carbohidratos) + 9 * grasa + 7 * alcohol

print(f'Las calorías totales del producto son: {calorias}')
print(f'Las calorías totales del producto son: {math.ceil(calorias)}')