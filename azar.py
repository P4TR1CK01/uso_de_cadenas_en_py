import random
def main ():
  ganador = random.randint(1, 10)

  while True:
    opcion = int(input('Adivine un numero entre 1 y 10: '))
    if opcion == ganador:
      print('Felicidades ganaste')
      break

    else:
      print('Felicidades perdiste')
#main()

def tablas():
  i = 1
  while i <= 10:
    print('\nLa tabla de ' + str(i))
    j=1
    while j <= 10:
      frase = str(i) + 'x' + str(j) + '=' + str(i*j)
      print(frase)
      j += 1
    i += 1

tablas ()