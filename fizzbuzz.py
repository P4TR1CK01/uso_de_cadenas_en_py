def fizzbuzz (inicio, final):
  i = inicio
  while i <= final:
    if i % 3 == 0 and i % 5 == 0:
      print ('FizzBuzz')
    elif i % 3 == 0:
      print('Fizz')
    elif i % 5 == 0:
      print('Buzz')
    else: 
      print (i)
    i +=  1

fizzbuzz (800 , 1123)


def validarPassword (password)
  password