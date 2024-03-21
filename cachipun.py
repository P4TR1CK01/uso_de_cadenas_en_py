'''Vamos a jugar cachipun con el usuario.'''

import random

# 1. Vamos a pedir la jugada del usuario 

jugada_usuario = input('Ingrese su jugada:\n1:piedra\n2: papel\n3: tijera\n')

if jugada_usuario == '1':
    print('Usted eligió piedra')
elif jugada_usuario == '2':
    print('Usted eligió papel')
elif jugada_usuario == '3':
    print('Usted eligió tijera')

# 2. Generarvalor aleatorio con randit(a,b)
    
jugada_cpu = random.randint(1,3)

#3. Transformo la jugada del computador a string

jugada_cpu = str(jugada_cpu)

print('jugada del computador:', jugada_cpu)

#4. Determinar el ganador

if jugada_usuario == '1':             #Usuario elige piedra
    if jugada_cpu == '1':             #Computador elige piedra
        print('Empate: Ambos eligieron piedra')
    elif jugada_cpu == '2':           #Computador elige papel        
        print('cpu gana: papel contra piedra')
    elif jugada_cpu == '3':          #Computador elige tijera
        print('gana usted: piedra le gana a tijera')    

elif jugada_usuario == '2':           #Usuario elige papel
        if jugada_cpu == '1':         #Computador elige piedra
            print('gana usuario: papel le gana a piedra')
        elif jugada_cpu == '2':       #Computador elige papel
            print('Empate: Ambos eligieron papel')
        elif jugada_cpu == '3':      #Computador elige tijera
            print('gana cpu: tijera le gana a papel')
        
elif jugada_usuario == '3':             #Usuario elige tijera
  
            if jugada_cpu == '1':             #Computador elige piedra
                print('gana cpu: piedra le gana a tijera')
            elif jugada_cpu == '2':           #Computador elige papel
                print('gana usuario: tijera le gana a papel')
            elif jugada_cpu == '3':      #Computador elige tijera
                print('Empate: Ambos eligieron tijera')

else:      
    print('Jugada no válida')
  
