'''
2. Supongamos ahora que el emprendedor considera 2 tipos de usuarios diferenciados,
los usuarios normales y los usuarios premium a los cuales se les cobrará una
suscripción un 50% mayor. Crea una segunda versión llamada emprendedor2.py que
permita considerar el caso recién expuesto. Para ello modifica la fórmula de utilidades
en la cual se solicite mediante input() los parámetros de entrada precios de
suscripción P, así como el número de usuarios Unormal y Upremium y el gasto total GT.
(3 Puntos)
'''

                                          #creamos el programa emprendedor2.py

#la formula para calcular las utilidades de un proyecto es:  utilidades = (P*U) - GT


def calculo_utilidades():                                          #definimos la funcion calculo_utilidades

  P = float(input('Ingrese el precio de suscripción: '))           #pedimos al usuario que ingrese el precio de suscripcion
  U = float(input('Ingrese el número de usuarios normales: '))     #pedimos al usuario que ingrese el numero de usuarios
  UP = float(input('Ingrese el número de usuarios premium: '))     #pedimos al usuario que ingrese el numero de usuarios premium
  GT = float(input('Ingrese el gasto total: '))                    #pedimos al usuario que ingrese el gasto total
  
  utilidades =((P*U) + (1.5*P*UP)) - GT                            #calculamos las utilidades 

  print('Las utilidades del proyecto son: ', utilidades)           #imprimimos las utilidades          

calculo_utilidades() 






'''def calculo_utilidades():: Esta línea define una función llamada calculo_utilidades.'''
'''P = float(input('Ingrese el precio de suscripción: ')): Esta línea pide al usuario que ingrese el precio de suscripción y convierte la entrada del usuario a un número de punto flotante.'''
'''U = float(input('Ingrese el número de usuarios normales: ')): Similar a la línea anterior, esta línea pide al usuario que ingrese el número de usuarios y convierte la entrada del usuario a un número de punto flotante.'''
'''UP = float(input('Ingrese el número de usuarios premium: ')): Similar a las líneas anteriores, esta línea pide al usuario que ingrese el número de usuarios premium y convierte la entrada del usuario a un número de punto flotante.'''
'''GT = float(input('Ingrese el gasto total: ')): Similar a las líneas anteriores, esta línea pide al usuario que ingrese el gasto total y convierte la entrada del usuario a un número de punto flotante.'''
'''utilidades =((P*U) + (1.5*P*UP)) - GT: Esta línea calcula las utilidades utilizando la fórmula de utilidades y los valores ingresados por el usuario.'''
'''print('Las utilidades del proyecto son: ', utilidades): Esta línea imprime las utilidades calculadas.'''
'''calculo_utilidades(): Esta línea llama a la función calculo_utilidades, lo que hace que se ejecute el código dentro de la función.'''
'''La función calculo_utilidades solicita al usuario que ingrese el precio de suscripción, el número de usuarios normales, el número de usuarios premium y el gasto total, y luego calcula las utilidades utilizando la fórmula de utilidades. Finalmente, imprime las utilidades calculadas.'''
'''La función float convierte una cadena en un número de punto flotante. En este caso, se utiliza para convertir la entrada del usuario en un número decimal.'''
'''En este caso, la función calculo_utilidades realiza el cálculo de las utilidades de un proyecto.'''
'''La fórmula para calcular las utilidades de un proyecto es: utilidades = (P*U) - GT. En este caso, se ha modificado la fórmula para considerar dos tipos de usuarios diferenciados, los usuarios normales y los usuarios premium, a los cuales se les cobra una suscripción un 50% mayor. La fórmula modificada es: utilidades = (P*U) + (1.5*P*UP) - GT, donde P es el precio de suscripción, U es el número de usuarios normales, UP es el número de usuarios premium y GT es el gasto total.'''
'''La función round redondea un número a un número específico de decimales. En este caso, se utiliza para redondear las utilidades a 2 decimales.'''
