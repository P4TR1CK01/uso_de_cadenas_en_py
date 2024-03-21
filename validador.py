import getpass

def validarPassword(password):
  #validamos que sea de largo almenos 6
  if len(password) < 6:
    print('Su contraseña debe contener al menos 6 caracteres')
    return False
  elif password == '12345678':
    print('este password es muy sencillo. Porfavor elija otro')
    return False
  elif password == '87654321':
    print('este password es muy sencillo. Porfavor elija otro')
    return False
  elif "'" in password or ('"' in password) or ('*' in password):
    print("no puede usar el caracter ' dentro de su password")
    return False
  else:
    print('Contraseña correcta')
    return True
  #elif not any(['*', '~', '?', '¿'] in password):

def main():
  while True:         # 1. Le pido la nueva contraseña al usuario
    password = getpass.getpass('Ingrese una contraseña: ')  # 2. Valido la contraseña usando la funcion 'validarPassword'
    esCorrecta = validarPassword(password)  # Si la contraseña es incorrecta, repetimos el ciclo
    if esCorrecta:    # Si es correcta, terminamos el ciclo
      break           # Ya terminamos el ciclo, entonces la contraseña esta bien
  print('Bienvenidos al sistema')
main()









'''
/a*a/
"abba"      T
"casa"      F
"alabama"   T
"pera"      F
"arkansas"  F

#regex o expreciones regulares
patron = /e.*r/ #el punto representa 0 o más

"esmeril"   F
"ecuador"   T
'''
