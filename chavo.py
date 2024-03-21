''''

numero = int(input('ingrese un numero: '))
maquina = numero + 1
string = str(maquina)
mensaje = 'el numero que gana es '

print(mensaje + string)

'''

# 1. Le pido al usuario que ingrese un numero
num_usuario = input('ingrese un numero: ')
# 2. Transformar el stringing ingresado a numero
num_usuario = int(num_usuario)
# 3. Le sumo 1 al numero del usuario
num_comp = num_usuario + 1
# 4. Transformo el numero de la computadora a string
num_comp = str(num_comp)
# 5. Creo la variable mensaje
mensaje = 'Yo gané con el numero ' + num_comp
# 6. Le aviso al usuario del mensaje
print(mensaje)
####

'''
print('Gano con el ' + str(int(input('ingrese un numero: ')) + 1))
'''