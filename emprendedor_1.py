####Actividad 2 - Rentabilidad
'''
1. Crear el programa emprendedor1.py que utilice la fórmula descrita anteriormente
para calcular las utilidades de un proyecto. Para ello utiliza input() para solicitar
como dato el precio de suscripción P, el número de usuarios U y el gasto total GT.
(5 Puntos)



Nota: Dentro de las instrucciones del programa advierte al usuario de valores
que podrían impedir un buen funcionamiento de éste.

'''

                                          #creamos el programa emprendedor1.py

#la formula para calcular las utilidades de un proyecto es:  utilidades = (P*U) - GT


def calculo_utilidades():                                #definimos la funcion calculo_utilidades

  P = float(input('Ingrese el precio de suscripción: '))  #pedimos al usuario que ingrese el precio de suscripcion
  U = float(input('Ingrese el número de usuarios: '))     #pedimos al usuario que ingrese el numero de usuarios
  GT = float(input('Ingrese el gasto total: '))           #pedimos al usuario que ingrese el gasto total
  utilidades = (P*U) - GT                                 #calculamos las utilidades
  
  print('Las utilidades del proyecto son: ', utilidades)  #imprimimos las utilidades          

calculo_utilidades()                                      #llamamos a la funcion calculo_utilidades





'''def calculo_utilidades():: Esta línea define una función llamada calculo_utilidades. Las funciones son bloques de código reutilizables que realizan una acción específica.'''
'''P = float(input('Ingrese el precio de suscripción: ')): Esta línea pide al usuario que ingrese el precio de suscripción y convierte la entrada del usuario a un número de punto flotante.'''
'''U = float(input('Ingrese el número de usuarios: ')): Similar a la línea anterior, esta línea pide al usuario que ingrese el número de usuarios y convierte la entrada del usuario a un número de punto flotante.'''
'''GT = float(input('Ingrese el gasto total: ')): Similar a las líneas anteriores, esta línea pide al usuario que ingrese el gasto total y convierte la entrada del usuario a un número de punto flotante.'''
'''utilidades = (P*U) - GT: Esta línea calcula las utilidades utilizando la fórmula de utilidades y los valores ingresados por el usuario.'''
'''print('Las utilidades del proyecto son: ', utilidades): Esta línea imprime las utilidades calculadas.'''
'''calculo_utilidades(): Esta línea llama a la función calculo_utilidades, lo que hace que se ejecute el código dentro de la función.'''
'''La función calculo_utilidades solicita al usuario que ingrese el precio de suscripción, el número de usuarios y el gasto total, y luego calcula las utilidades utilizando la fórmula de utilidades. Finalmente, imprime las utilidades calculadas.'''
