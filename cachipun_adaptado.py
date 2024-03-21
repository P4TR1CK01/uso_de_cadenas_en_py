#Cachipún
'''El Cachipún, conocido también como chinchanpu,pikachú,jankenpón, yankenpo, pinpon
papas, hakembó o how-are-you-speak, es un juego de manos en el que existen tres
elementos: la piedra que vence a la tijera rompiéndola, la tijera que vence al papel cortándolo
y el papel que vence a la piedra envolviéndola, dando lugar a un círculo o ciclo cerrado. Se
utiliza con mucha frecuencia para decidir quién de dos personas hará algo, tal y como se
hace a veces usando una moneda, o para dirimir algún asunto.

Para poner en práctica lo que hemos aprendido a lo largo de la unidad, se implementará un
programa en Python que permite jugar al cachipún en contra del computador.

Se pide crear el programa cachipun.py, donde el usuario entregará como
argumento: piedra, papel o tijera. Para que el computador pueda jugar escogerá un
valor al azar. Para eso se solicita investigar random.choice() de la librería random.

#Considerar las opciones de ganar, perder o empatar con la computadora.

#En caso que el argumento sea distinto a piedra, papel o tijera, el programa debe
mostrar las opciones que se pueden jugar
Argumento inválido: Debe ser piedra, papel o tijera.
'''
#empezamos con la instrucción del programa

import random

# 1. Vamos a pedir la jugada del usuario

jugada_usuario = input('Ingrese su jugada:\n1:piedra\n2: papel\n3: tijera\n')

if jugada_usuario == 'piedra':
    print('Usted eligió piedra')
elif jugada_usuario == 'papel':
    print('Usted eligió papel')
elif jugada_usuario == 'tijera':
    print('Usted eligió tijera')

# 2. Generarvalor aleatorio con randit(a,b)

jugada_cpu = random.randint(1,3) #randit hace un número aleatorio entre 1 y 3

#3. Transformo la jugada del computador a string

jugada_cpu = str(jugada_cpu)
