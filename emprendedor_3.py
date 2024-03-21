'''
3. Considera ahora una tercera versión llamada emprendedor3.py utilizando la fórmula
original de utilidades donde el usuario ingrese el precio de suscripción P, el número de
usuarios normales U y los gastos GT. Adicionalmente, solicita las utilidades del año
anterior Uanterior, todo esto mediante input(). El programa debe calcular las utilidades
actuales y mostrar la razón entre las utilidades actuales y las del año anterior con dos
decimales.
(2 Puntos)
'''
                                          #creamos el programa emprendedor3.py

#la formula para calcular las utilidades de un proyecto es:  utilidades = (P*U) - GT 


def calculo_utilidades():                                                   #definimos la funcion calculo_utilidades

    P = float(input('Ingrese el precio de suscripción: '))                  #pedimos al usuario que ingrese el precio de suscripcion
    U = float(input('Ingrese el número de usuarios normales: '))            #pedimos al usuario que ingrese el numero de usuarios
    UP = float(input('ingrese el nmero de usuarios premium:'))              #pedimos al usario que ingrese el numero de usuarios premium
    GT = float(input('ingrese el gasto total: '))                           #pedimos al usuario que ingrese el gasto total
    Uanterior = float(input('ingrese las utilidades del año anterior: '))   #pedimos al usuario que ingrese las utilidades del año anterior
  
    utilidades_actuales = ((P*U) + (1.5*P*UP)) - GT                         #calculamos las utilidades  
    razon = utilidades_actuales/Uanterior                                   #calculamos la razon entre las utilidades actuales y las del año anterior

    print('Las utilidades actuales son: ', round(utilidades_actuales,2))     #imprimimos las utilidades actuales utilizando la funcion round para redondear a 2 decimales

calculo_utilidades()




'''def calculo_utilidades():: Esta línea define una función llamada calculo_utilidades.'''
'''P = float(input('Ingrese el precio de suscripción: ')): Esta línea pide al usuario que ingrese el precio de suscripción y convierte la entrada del usuario a un número de punto flotante.'''
'''U = float(input('Ingrese el número de usuarios normales: ')): Esta línea pide al usuario que ingrese el número de usuarios y convierte la entrada del usuario a un número de punto flotante.'''
'''UP = float(input('ingrese el nmero de usuarios premium:')): Esta línea pide al usuario que ingrese el número de usuarios premium y convierte la entrada del usuario a un número de punto flotante.'''
'''GT = float(input('ingrese el gasto total: ')): Esta línea pide al usuario que ingrese el gasto total y convierte la entrada del usuario a un número de punto flotante.'''
'''utilidades_actuales = ((P*U) + (1.5*P*UP)) - GT: Esta línea calcula las utilidades actuales utilizando la fórmula de utilidades y los valores ingresados por el usuario.'''
'''razon = utilidades_actuales/Uanterior: Esta línea calcula la razón entre las utilidades actuales y las del año anterior.'''
'''print('Las utilidades actuales son: ', round(utilidades_actuales,2)): Esta línea imprime las utilidades actuales redondeadas a 2 decimales.'''
'''La función round redondea un número a un número específico de decimales. En este caso, se utiliza para redondear las utilidades actuales a 2 decimales.'''
'''calculo_utilidades(): Esta línea llama a la función calculo_utilidades, lo que hace que se ejecute el código dentro de la función.'''
'''La función calculo_utilidades solicita al usuario que ingrese el precio de suscripción, el número de usuarios normales, el número de usuarios premium, el gasto total y las utilidades del año anterior, y luego calcula las utilidades actuales y la razón entre las utilidades actuales y las del año anterior. Finalmente, imprime las utilidades actuales redondeadas a 2 decimales.'''
'''La fórmula para calcular las utilidades de un proyecto es: utilidades = (P*U) - GT. En este caso, se ha modificado la fórmula para considerar dos tipos de usuarios diferenciados, los usuarios normales y los usuarios premium, a los cuales se les cobra una suscripción un 50% mayor. La fórmula modificada es: utilidades = (P*U) + (1.5*P*UP) - GT, donde P es el precio de suscripción, U es el número de usuarios normales, UP es el número de usuarios premium y GT es el gasto total. Adicionalmente, se ha agregado el cálculo de la razón entre las utilidades actuales y las del año anterior.'''



