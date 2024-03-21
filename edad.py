# 1. Pido al usuario que ingrese su edad
edad = input ('Por favor ingrese su edad')
#transformo la edad al tipo 'int'
edad = int(edad)
# veo si el usuario puede votar
if edad < 18:
  print('Usted no puede votar')
elif edad >= 18 and edad < 65:
  print('Usted si puede votar. Haga la fila')
elif edad < 120:
  print('Usted si puede votar, y se puede saltar la fila')
else:
  print('Usted voto por Ohiggins')